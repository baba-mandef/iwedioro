from elevenlabs import generate, voice, voices, set_api_key, clone


class Iwedioro():
    model = 'eleven_multilingual_v2'
    token = 'None'

    def set_token(self, token):
        """
        This function take an api key as parameter and
        set it in client.
        Usefule to set another api ken when your token is expire
        """
        self.token = token
        set_api_key(token)

        return

    def get_voice_list(self) -> list:
        """
        This function help us to retrive available voices list"""
        voice_list = voices()

        return voice_list

    def add_voice(self, name, description, files):
        clone(
            name=name,
            description=description,
            files=files,
            labels={})

    def generate(self, text, voice, token=None):
        token = self.token
        print(token)
        generate(
            text=text,
            api_key=token,
            voice=voice,
            model=self.model,
            stream=False,
            stream_chunk_size=2048

        )

    def token_initialize(self):
        pass
