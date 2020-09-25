""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud._compat import CompactClient


class Client(CompactClient):
    def __init__(self, config: dict, transport=None, middleware=None):
        self._config = config
        super(Client, self).__init__(config, transport, middleware)

    def pathx(self):
        from ucloud.services.pathx.client import PathXClient

        return PathXClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def stepflow(self):
        from ucloud.services.stepflow.client import StepFlowClient

        return StepFlowClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def uaccount(self):
        from ucloud.services.uaccount.client import UAccountClient

        return UAccountClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def ucdn(self):
        from ucloud.services.ucdn.client import UCDNClient

        return UCDNClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def udb(self):
        from ucloud.services.udb.client import UDBClient

        return UDBClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def udpn(self):
        from ucloud.services.udpn.client import UDPNClient

        return UDPNClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def udisk(self):
        from ucloud.services.udisk.client import UDiskClient

        return UDiskClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def uhost(self):
        from ucloud.services.uhost.client import UHostClient

        return UHostClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def ulb(self):
        from ucloud.services.ulb.client import ULBClient

        return ULBClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def umem(self):
        from ucloud.services.umem.client import UMemClient

        return UMemClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def unet(self):
        from ucloud.services.unet.client import UNetClient

        return UNetClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def uphost(self):
        from ucloud.services.uphost.client import UPHostClient

        return UPHostClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def usms(self):
        from ucloud.services.usms.client import USMSClient

        return USMSClient(
            self._config, self.transport, self.middleware, self.logger
        )


    
    
    def ipsecvpn(self):
        from ucloud.services.ipsecvpn.client import IPSecVPNClient
        return IPSecVPNClient(self._config, self.transport, self.middleware, self.logger)
    

    
    

    
    

    
    
    def uapigateway(self):
        from ucloud.services.uapigateway.client import UAPIGatewayClient
        return UAPIGatewayClient(self._config, self.transport, self.middleware, self.logger)
    

    
    

    
    
    def uarchive(self):
        from ucloud.services.uarchive.client import UArchiveClient
        return UArchiveClient(self._config, self.transport, self.middleware, self.logger)
    

    
    
    def ubill(self):
        from ucloud.services.ubill.client import UBillClient
        return UBillClient(self._config, self.transport, self.middleware, self.logger)
    

    
    

    
    
    def ucloudstack(self):
        from ucloud.services.ucloudstack.client import UCloudStackClient
        return UCloudStackClient(self._config, self.transport, self.middleware, self.logger)
    

    
    

    
    
    def uddb(self):
        from ucloud.services.uddb.client import UDDBClient
        return UDDBClient(self._config, self.transport, self.middleware, self.logger)
    

    
    
    def uddos_uclean(self):
        from ucloud.services.uddos_uclean.client import UDDoS_UCleanClient
        return UDDoS_UCleanClient(self._config, self.transport, self.middleware, self.logger)
    

    
    
    def udhost(self):
        from ucloud.services.udhost.client import UDHostClient
        return UDHostClient(self._config, self.transport, self.middleware, self.logger)
    

    
    

    
    
    def udts(self):
        from ucloud.services.udts.client import UDTSClient
        return UDTSClient(self._config, self.transport, self.middleware, self.logger)
    

    
    

    
    
    def udocker(self):
        from ucloud.services.udocker.client import UDockerClient
        return UDockerClient(self._config, self.transport, self.middleware, self.logger)
    

    
    
    def uedn(self):
        from ucloud.services.uedn.client import UEDNClient
        return UEDNClient(self._config, self.transport, self.middleware, self.logger)
    

    
    
    def uewaf(self):
        from ucloud.services.uewaf.client import UEWAFClient
        return UEWAFClient(self._config, self.transport, self.middleware, self.logger)
    

    
    
    def ufs(self):
        from ucloud.services.ufs.client import UFSClient
        return UFSClient(self._config, self.transport, self.middleware, self.logger)
    

    
    
    def ufile(self):
        from ucloud.services.ufile.client import UFileClient
        return UFileClient(self._config, self.transport, self.middleware, self.logger)
    

    
    
    def ugc(self):
        from ucloud.services.ugc.client import UGCClient
        return UGCClient(self._config, self.transport, self.middleware, self.logger)
    

    
    

    
    
    def uhub(self):
        from ucloud.services.uhub.client import UHubClient
        return UHubClient(self._config, self.transport, self.middleware, self.logger)
    

    
    
    def uhybridv3(self):
        from ucloud.services.uhybridv3.client import UHybridV3Client
        return UHybridV3Client(self._config, self.transport, self.middleware, self.logger)
    

    
    
    def uk8s(self):
        from ucloud.services.uk8s.client import UK8SClient
        return UK8SClient(self._config, self.transport, self.middleware, self.logger)
    

    
    
    def ukms(self):
        from ucloud.services.ukms.client import UKMSClient
        return UKMSClient(self._config, self.transport, self.middleware, self.logger)
    

    
    
    def ukafka(self):
        from ucloud.services.ukafka.client import UKafkaClient
        return UKafkaClient(self._config, self.transport, self.middleware, self.logger)
    

    
    

    
    
    def ulive(self):
        from ucloud.services.ulive.client import ULiveClient
        return ULiveClient(self._config, self.transport, self.middleware, self.logger)
    

    
    
    def umai(self):
        from ucloud.services.umai.client import UMAIClient
        return UMAIClient(self._config, self.transport, self.middleware, self.logger)
    

    
    
    def umedia(self):
        from ucloud.services.umedia.client import UMediaClient
        return UMediaClient(self._config, self.transport, self.middleware, self.logger)
    

    
    

    
    
    def umon(self):
        from ucloud.services.umon.client import UMonClient
        return UMonClient(self._config, self.transport, self.middleware, self.logger)
    

    
    

    
    

    
    
    def urtc(self):
        from ucloud.services.urtc.client import URTCClient
        return URTCClient(self._config, self.transport, self.middleware, self.logger)
    

    
    

    
    
    def usql(self):
        from ucloud.services.usql.client import USQLClient
        return USQLClient(self._config, self.transport, self.middleware, self.logger)
    

    
    
    def uvideo(self):
        from ucloud.services.uvideo.client import UVideoClient
        return UVideoClient(self._config, self.transport, self.middleware, self.logger)
    

    
    
    def vpc(self):
        from ucloud.services.vpc.client import VPCClient
        return VPCClient(self._config, self.transport, self.middleware, self.logger)
    


    def vpc(self):
        from ucloud.services.vpc.client import VPCClient

        return VPCClient(
            self._config, self.transport, self.middleware, self.logger
        )
