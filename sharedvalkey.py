from glide import GlideClientConfiguration, NodeAddress, GlideClient

class SharedValkey:

    def __init__(self):
        addresses = [
             NodeAddress("localhost", 6379)
        ]
        self.config = GlideClientConfiguration(addresses)
        self.init = False
        self.valkey_client = None

    async def get_or_create_client(self):
        # Check if the client has NOT been initialized yet
        if not self.init:
            # Create the client instance
            self.valkey_client = await GlideClient.create(self.config)
            # Mark as initialized
            self.init = True
        # Return the existing (or newly created) client
        return self.valkey_client
