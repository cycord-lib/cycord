class Asset:
    __slots__: Tuple[str, ...] = (
        '_url',
        '_animated',
        '_key',
    )

    BASE = 'https://cdn.discordapp.com'

    def __init__(self, *, url: str, key: str, animated: bool = False) -> None:
        self._url: str = url
        self._animated: bool = animated
        self._key: str = key

    @classmethod
    def _from_default_avatar(cls, index: int) -> Self:
        return cls(
            url=f'{cls.BASE}/embed/avatars/{index}.png',
            key=str(index),
            animated=False,
        )

    @classmethod
    def _from_avatar(cls, user_id: int, avatar: str) -> Self:
        animated = avatar.startswith('a_')
        format = 'gif' if animated else 'png'
        return cls(
            url=f'{cls.BASE}/avatars/{user_id}/{avatar}.{format}?size=1024',
            key=avatar,
            animated=animated,
        )

    @classmethod
    def _from_guild_avatar(cls, guild_id: int, member_id: int, avatar: str) -> Self:
        animated = avatar.startswith('a_')
        format = 'gif' if animated else 'png'
        return cls(
            url=f"{cls.BASE}/guilds/{guild_id}/users/{member_id}/avatars/{avatar}.{format}?size=1024",
            key=avatar,
            animated=animated,
        )

    @classmethod
    def _from_guild_banner(cls, guild_id: int, member_id: int, banner: str) -> Self:
        animated = banner.startswith('a_')
        format = 'gif' if animated else 'png'
        return cls(
            url=f"{cls.BASE}/guilds/{guild_id}/users/{member_id}/banners/{banner}.{format}?size=1024",
            key=banner,
            animated=animated,
        )

    @classmethod
    def _from_avatar_decoration(cls, avatar_decoration: str) -> Self:
        return cls(
            url=f'{cls.BASE}/avatar-decoration-presets/{avatar_decoration}.png?size=96',
            key=avatar_decoration,
            animated=True,
        )

    @classmethod
    def _from_icon(cls, object_id: int, icon_hash: str, path: str) -> Self:
        return cls(
            url=f'{cls.BASE}/{path}-icons/{object_id}/{icon_hash}.png?size=1024',
            key=icon_hash,
            animated=False,
        )

    @classmethod
    def _from_app_icon(
        cls, object_id: int, icon_hash: str, asset_type: Literal['icon', 'cover_image']
    ) -> Self:
        return cls(
            url=f'{cls.BASE}/app-icons/{object_id}/{asset_type}.png?size=1024',
            key=icon_hash,
            animated=False,
        )

    @classmethod
    def _from_cover_image(cls, object_id: int, cover_image_hash: str) -> Self:
        return cls(
            url=f'{cls.BASE}/app-assets/{object_id}/store/{cover_image_hash}.png?size=1024',
            key=cover_image_hash,
            animated=False,
        )

    @classmethod
    def _from_scheduled_event_cover_image(cls, scheduled_event_id: int, cover_image_hash: str) -> Self:
        return cls(
            url=f'{cls.BASE}/guild-events/{scheduled_event_id}/{cover_image_hash}.png?size=1024',
            key=cover_image_hash,
            animated=False,
        )

    @classmethod
    def _from_guild_image(cls, guild_id: int, image: str, path: str) -> Self:
        animated = image.startswith('a_')
        format = 'gif' if animated else 'png'
        return cls(
            url=f'{cls.BASE}/{path}/{guild_id}/{image}.{format}?size=1024',
            key=image,
            animated=animated,
        )

    @classmethod
    def _from_guild_icon(cls, guild_id: int, icon_hash: str) -> Self:
        animated = icon_hash.startswith('a_')
        format = 'gif' if animated else 'png'
        return cls(
            url=f'{cls.BASE}/icons/{guild_id}/{icon_hash}.{format}?size=1024',
            key=icon_hash,
            animated=animated,
        )

    @classmethod
    def _from_sticker_banner(cls, banner: int) -> Self:
        return cls(
            url=f'{cls.BASE}/app-assets/710982414301790216/store/{banner}.png',
            key=str(banner),
            animated=False,
        )

    @classmethod
    def _from_user_banner(cls, user_id: int, banner_hash: str) -> Self:
        animated = banner_hash.startswith('a_')
        format = 'gif' if animated else 'png'
        return cls(
            url=f'{cls.BASE}/banners/{user_id}/{banner_hash}.{format}?size=512',
            key=banner_hash,
            animated=animated,
        )

    def __str__(self) -> str:
        return self._url

    def __len__(self) -> int:
        return len(self._url)

    def __repr__(self) -> str:
        shorten = self._url.replace(self.BASE, '')
        return f'<Asset url={shorten!r}>'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Asset) and self._url == other._url

    def __hash__(self) -> int:
        return hash(self._url)

    @property
    def url(self) -> str:
        return self._url

    @property
    def key(self) -> str:
        return self._key

    def is_animated(self) -> bool:
        return self._animated

    def replace(
        self,
        *,
        size: int = MISSING,
        format: ValidAssetFormatTypes = MISSING,
        static_format: ValidStaticFormatTypes = MISSING,
    ) -> Self:
        url = yarl.URL(self._url)
        path, _ = os.path.splitext(url.path)

        if format is not MISSING:
            if self._animated:
                if format not in VALID_ASSET_FORMATS:
                    raise ValueError(f'format must be one of {VALID_ASSET_FORMATS}')
            else:
                if static_format is MISSING and format not in VALID_STATIC_FORMATS:
                    raise ValueError(f'format must be one of {VALID_STATIC_FORMATS}')
            url = url.with_path(f'{path}.{format}')

        if static_format is not MISSING and not self._animated:
            if static_format not in VALID_STATIC_FORMATS:
                raise ValueError(f'static_format must be one of {VALID_STATIC_FORMATS}')
            url = url.with_path(f'{path}.{static_format}')

        if size is not MISSING:
            if not utils.valid_icon_size(size):
                raise ValueError('size must be a power of 2 between 16 and 4096')
            url = url.with_query(size=size)
        else:
            url = url.with_query(url.raw_query_string)

        url = str(url)
        return self.__class__(url=url, key=self._key, animated=self._animated)

    def with_size(self, size: int, /) -> Self:
        if not utils.valid_icon_size(size):
            raise ValueError('size must be a power of 2 between 16 and 4096')

        url = str(yarl.URL(self._url).with_query(size=size))
        return self.__class__(url=url, key=self._key, animated=self._animated)

    def with_format(self, format: ValidAssetFormatTypes, /) -> Self:
        if self._animated:
            if format not in VALID_ASSET_FORMATS:
                raise ValueError(f'format must be one of {VALID_ASSET_FORMATS}')
        else:
            if format not in VALID_STATIC_FORMATS:
                raise ValueError(f'format must be one of {VALID_STATIC_FORMATS}')

        url = yarl.URL(self._url)
        path, _ = os.path.splitext(url.path)
        url = str(url.with_path(f'{path}.{format}').with_query(url.raw_query_string))
        return self.__class__(url=url, key=self._key, animated=self._animated)

    def with_static_format(self, format: ValidStaticFormatTypes, /) -> Self:
        if self._animated:
            return self
        return self.with_format(format)