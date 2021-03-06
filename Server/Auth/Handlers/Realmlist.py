from struct import pack

from World.WorldPacket.Constants.LoginOpCode import LoginOpCode
from World.Realmlist.Sandbox.Sandbox import realm
from Realm.Constants.RealmPopulation import RealmPopulation
from Realm.Constants.RealmFlags import RealmFlags


class Realmlist(object):

    REALMLIST_RESPONSE_HEADER_FORMAT = '<HIH'
    REALMLIST_RESPONSE_FOOTER_FORMAT = '<B'
    MIN_RESPONSE_SIZE = 7

    def __init__(self, **kwargs):
        pass

    async def process(self) -> tuple:
        realm_packet = realm.get_state_packet(RealmFlags.NORMAL.value, RealmPopulation.LOW.value)
        realm_packet_as_bytes = b''.join([realm_packet])

        # TODO: should be moved to constants since more than one realm will exists
        num_realms = 1

        header = pack(
            Realmlist.REALMLIST_RESPONSE_HEADER_FORMAT,
            Realmlist.MIN_RESPONSE_SIZE + len(realm_packet_as_bytes),
            0x00,
            num_realms
        )

        footer = pack(Realmlist.REALMLIST_RESPONSE_FOOTER_FORMAT, 0)

        response = header + realm_packet_as_bytes + footer

        return LoginOpCode.REALMLIST, [response]
