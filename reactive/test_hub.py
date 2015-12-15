from charms.reactive import when, when_not, set_state, remove_state
from charmhelpers.core import hookenv


@when_not('hub.connected')
def blocked():
    hookenv.status_set('blocked', 'Waiting for relation to Hub')
    remove_state('registered')


@when('hub.connected')
@when_not('registered')
def register(hub):
    hub.register_service('hub-test', {
        'message': 'This is a test of the Big Data Hub',
    })
    hookenv.status_set('waiting', 'Registered and looking')
    set_state('registered')


@when('hub.service.hub-test')
def report(hub):  # pylint: disable=unused-argument
    hookenv.status_set('active', 'I can see myself!')
