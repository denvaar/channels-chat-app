from channels import Group
from channels.sessions import channel_session, enforce_ordering


@enforce_ordering(slight=True)
@channel_session
def ws_connect(message):
    room = message.content['path'].strip('/')
    message.channel_session['room'] = room
    Group('chat-{}'.format(room)).add(message.reply_channel)


@enforce_ordering(slight=True)
@channel_session
def ws_message(message):
    Group('chat-{}'.format(message.channel_session['room'])).send({
        'text': message['text'],
    })


@enforce_ordering(slight=True)
@channel_session
def ws_disconnect(message):
    Group('chat-{}'.format(message.channel_session['room'])).discard(
        message.reply_channel)
