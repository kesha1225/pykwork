import typing
import pydantic


class Achievements(pydantic.BaseModel):
    pass


class KworkBadges(pydantic.BaseModel):
    pass


class InboxOrder(pydantic.BaseModel):
    order_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID заказа",
    )
    status: typing.Optional[str] = pydantic.Field(
        None,
        description="Состояние предложения: new - Предложение в силе, cancel - Отказ, done - Заказ создан",
    )
    budget: typing.Optional[int] = pydantic.Field(
        None,
        description="Бюджет",
    )
    duration: typing.Optional[int] = pydantic.Field(
        None,
        description="срок выполнения (секунд); null - срок не ограничен",
    )
    kwork: typing.Optional[dict] = pydantic.Field(
        None,
        description="Объект кворка",
    )
    order: typing.Optional[dict] = pydantic.Field(
        None,
        description="Объект заказа",
    )


class TrackOrder(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID заказа",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Название заказа",
    )
    color: typing.Optional[int] = pydantic.Field(
        None,
        description="Цвет заказа",
    )
    worker_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID продавца",
    )


class Portfolio(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Название работы",
    )
    order_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID заказа",
    )
    category_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID категории заказа",
    )
    category_name: typing.Optional[str] = pydantic.Field(
        None,
        description="Название категории заказа",
    )
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="Тип, 'photo' или 'видео'",
    )
    photo: typing.Optional[str] = pydantic.Field(
        None,
        description="Относительный путь к фото",
    )
    video: typing.Optional[str] = pydantic.Field(
        None,
        description="Относительный путь к видео",
    )
    likes: typing.Optional[int] = pydantic.Field(
        None,
        description="Кол-во чистых лайков",
    )
    likes_dirty: typing.Optional[int] = pydantic.Field(
        None,
        description="Кол-во грязных лайков",
    )
    views: typing.Optional[int] = pydantic.Field(
        None,
        description="Кол-во чистых просмотров",
    )
    views_dirty: typing.Optional[int] = pydantic.Field(
        None,
        description="Кол-во грязных просмотров",
    )
    comments_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Кол-во комментариев",
    )
    is_liked: typing.Optional[bool] = pydantic.Field(
        None,
        description="Стоит ли лайк пользователя",
    )
    images: typing.Optional[typing.List[dict]] = pydantic.Field(
        None,
        description="Изображения, прикрепленные к портфолио",
    )
    videos: typing.Optional[typing.List[dict]] = pydantic.Field(
        None,
        description="Видеоролики, прикрепленные к портфолио",
    )


class ProfilePortfolios(pydantic.BaseModel):
    pass


class UserAnswer(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор ответа",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Текст ответа",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор пользователя - продавца",
    )
    time_added: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата ответа UNIXTIME",
    )
    username: typing.Optional[str] = pydantic.Field(
        None,
        description="Имя пользователя",
    )
    profilepicture: typing.Optional[str] = pydantic.Field(
        None,
        description="""Ссылка на изображения аватара
	 *     пользователя""",
    )


class ProfileKworks(pydantic.BaseModel):
    pass


class UserWorker(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор продавца",
    )
    username: typing.Optional[str] = pydantic.Field(
        None,
        description="Имя пользователя",
    )
    fullname: typing.Optional[str] = pydantic.Field(
        None,
        description="Полное имя пользователя",
    )
    profilepicture: typing.Optional[str] = pydantic.Field(
        None,
        description="Путь к аватару",
    )
    rating: typing.Optional[int] = pydantic.Field(
        None,
        description="Рейтинг по пятибальной шкале",
    )
    reviews_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Общее количество отзывов",
    )
    rating_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество отзывов",
    )
    is_online: typing.Optional[bool] = pydantic.Field(
        None,
        description="Онлайн ли пользователь",
    )


class ProfileBadges(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Название",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Описание",
    )
    image_url: typing.Optional[str] = pydantic.Field(
        None,
        description="Ссылка на изображение",
    )


class UserReviewWriter(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор продавца",
    )
    username: typing.Optional[str] = pydantic.Field(
        None,
        description="Имя пользователя",
    )
    profilepicture: typing.Optional[str] = pydantic.Field(
        None,
        description="Ссылка на изображения аватара пользователя",
    )


class WantWorker(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID запроса(проекта)",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID пользователя",
    )
    username: typing.Optional[str] = pydantic.Field(
        None,
        description="Логин пользователя",
    )
    profile_picture: typing.Optional[str] = pydantic.Field(
        None,
        description="Изображение профиля",
    )
    price: typing.Optional[int] = pydantic.Field(
        None,
        description="Бюджет проекта",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Заголовок",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Краткое описание проекта",
    )
    offers: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество предложений",
    )
    time_left: typing.Optional[int] = pydantic.Field(
        None,
        description="Время, оставшееся до закрытия проекта UNIX",
    )
    parent_category_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор рубрики проекта",
    )
    category_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор подрубрики проекта",
    )
    date_confirm: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата первого подтверждения модератором (или переподтвержения при перезапуске из архива)",
    )
    category_base_price: typing.Optional[int] = pydantic.Field(
        None,
        description="Базовая стоимость работ в категории запроса",
    )
    user_projects_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество проектов на бирже покупателя",
    )
    user_hired_percent: typing.Optional[int] = pydantic.Field(
        None,
        description="Процент нанятых продавцов на бирже",
    )
    achievements_list: typing.Optional[typing.List["Achievements"]] = pydantic.Field(
        None,
        description="",
    )
    is_viewed: typing.Optional[bool] = pydantic.Field(
        None,
        description="Просмотрен ли текущим пользователем",
    )
    already_work: typing.Optional[int] = pydantic.Field(
        None,
        description="Статус последнего заказа между пользователями",
    )
    allow_higher_price: typing.Optional[bool] = pydantic.Field(
        None,
        description="Готов ли покупатель рассмотреть предложения с ценой выше",
    )
    possible_price_limit: typing.Optional[int] = pydantic.Field(
        None,
        description="Лимит цены предложений с учетом готовности покупателя рассмотреть предложения с ценой выше",
    )


class TrackQuote(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор сообщения",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Текст сообщения",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор отправителя",
    )
    files: typing.Optional[typing.List["TrackFile"]] = pydantic.Field(
        None,
        description="Данные об изображениях",
    )


class Achievement(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Название",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Описание",
    )
    image_url: typing.Optional[str] = pydantic.Field(
        None,
        description="Ссылка на изображение",
    )


class VolumeType(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Наименование в единственном числе",
    )
    name_short: typing.Optional[str] = pydantic.Field(
        None,
        description="Сокращенное наименование",
    )
    name_plural_2_4: typing.Optional[str] = pydantic.Field(
        None,
        description="Наименование во множественном числе, от 2 до 4",
    )
    name_plural_11_19: typing.Optional[str] = pydantic.Field(
        None,
        description="Наименование во множественном числе, от 11 до 19",
    )
    name_accusative: typing.Optional[str] = pydantic.Field(
        None,
        description="Наименование в винительном падеже",
    )
    volume_type_group_id: typing.Optional[str] = pydantic.Field(
        None,
        description="Идентификатор группы объема услуг",
    )
    contains_value: typing.Optional[str] = pydantic.Field(
        None,
        description="Количество в других единицах",
    )
    contains_id: typing.Optional[str] = pydantic.Field(
        None,
        description="Единица объема для contains_value",
    )
    group_order: typing.Optional[str] = pydantic.Field(
        None,
        description="Сортировка для группы",
    )
    lang: typing.Optional[str] = pydantic.Field(
        None,
        description="Язык",
    )


class PositiveReviewsCount(pydantic.BaseModel):
    pass


class Category(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Название",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Описание",
    )


class ComplainCategory(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Название",
    )
    commentRequired: typing.Optional[bool] = pydantic.Field(
        None,
        description="Обязателен ли комментарий для данной категории жалоб",
    )
    isFileUploaderNotAuth: typing.Optional[bool] = pydantic.Field(
        None,
        description="Разрешено ли загружать файлы",
    )
    hasNotification: typing.Optional[bool] = pydantic.Field(
        None,
        description="Название",
    )
    subCategories: typing.Optional[typing.List["ComplainCategory"]] = pydantic.Field(
        None,
        description="Подкатегории жалобы",
    )


class KworkLinkSiteItem(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Наименование площадки/сайта/домена",
    )
    sqi: typing.Optional[str] = pydantic.Field(
        None,
        description="ИКС",
    )
    moz_domain_authority: typing.Optional[str] = pydantic.Field(
        None,
        description="Moz Domain Authority",
    )
    moz_spam_score: typing.Optional[str] = pydantic.Field(
        None,
        description="Moz Spam Score",
    )
    majestic_citation_flow: typing.Optional[str] = pydantic.Field(
        None,
        description="Majestic",
    )
    trust: typing.Optional[str] = pydantic.Field(
        None,
        description="Траст",
    )
    spam: typing.Optional[str] = pydantic.Field(
        None,
        description="Спам",
    )
    language: typing.Optional[str] = pydantic.Field(
        None,
        description="Язык",
    )
    traffic: typing.Optional[str] = pydantic.Field(
        None,
        description="Трафик (поле присутствует у площадки и сайта)",
    )


class File(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор файла",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Имя файла",
    )
    path: typing.Optional[str] = pydantic.Field(
        None,
        description="Путь к файлу",
    )


class ShortUserInfo(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор юзера",
    )
    username: typing.Optional[str] = pydantic.Field(
        None,
        description="Имя юзера",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Описание",
    )
    profilepicture: typing.Optional[str] = pydantic.Field(
        None,
        description="Аватар",
    )
    rating: typing.Optional[int] = pydantic.Field(
        None,
        description="Рейтинг по пятибальной шкале",
    )
    rating_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Кол-во оценок",
    )
    reviews_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Кол-во ревью",
    )
    good_reviews: typing.Optional[int] = pydantic.Field(
        None,
        description="Кол-во положительных отзывов",
    )
    bad_reviews: typing.Optional[int] = pydantic.Field(
        None,
        description="Кол-во отрицательных отзывов",
    )
    is_online: typing.Optional[bool] = pydantic.Field(
        None,
        description="Онлайн ли юзер",
    )
    level: typing.Optional[str] = pydantic.Field(
        None,
        description="Уровень пользователя",
    )
    location: typing.Optional[str] = pydantic.Field(
        None,
        description="Местонахождение и местное время",
    )
    order_done_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Кол-во выполненных заказов",
    )
    answer_time: typing.Optional[str] = pydantic.Field(
        None,
        description="Время ответа",
    )
    registration_time: typing.Optional[int] = pydantic.Field(
        None,
        description="Время регистрации UNIXTIME",
    )
    achievments_list: typing.Optional[typing.List["ProfileBadges"]] = pydantic.Field(
        None,
        description="Массив объектов наград",
    )


class KworkPackage(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Название",
    )
    package_description: typing.Optional[str] = pydantic.Field(
        None,
        description="Описание",
    )
    price: typing.Optional[int] = pydantic.Field(
        None,
        description="Стоимость пакета",
    )
    term: typing.Optional[str] = pydantic.Field(
        None,
        description="Срок выполнения",
    )
    min: typing.Optional[int] = pydantic.Field(
        None,
        description="Минимальное значение",
    )
    max: typing.Optional[int] = pydantic.Field(
        None,
        description="Максимальное значение",
    )
    options: typing.Optional[typing.List[dict]] = pydantic.Field(
        None,
        description="Опции пакета",
    )


class KworkInList(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор",
    )
    category_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID категории",
    )
    classifier_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID атрибута-значения классификации",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Название кворка",
    )
    image_url: typing.Optional[str] = pydantic.Field(
        None,
        description="Относительный путь к обложке кворка",
    )
    price: typing.Optional[int] = pydantic.Field(
        None,
        description="Стоимость кворка",
    )
    is_price_from: typing.Optional[bool] = pydantic.Field(
        None,
        description="Необходима ли подпись 'Цена ОТ'",
    )
    is_best: typing.Optional[bool] = pydantic.Field(
        None,
        description="Кворк имеет высший рейтинг",
    )
    is_hidden: typing.Optional[bool] = pydantic.Field(
        None,
        description="Кворк скрыт у активного юзера",
    )
    is_favorite: typing.Optional[bool] = pydantic.Field(
        None,
        description="Кворк в избранных у активного юзера",
    )
    is_viewed: typing.Optional[bool] = pydantic.Field(
        None,
        description="Просмотрен ли кворк",
    )
    isSubscription: typing.Optional[bool] = pydantic.Field(
        None,
        description="Кворк с подпиской?",
    )
    lang: typing.Optional[str] = pydantic.Field(
        None,
        description="Язык кворка, для привзяки валюты",
    )
    worker: typing.Optional["UserWorker"] = pydantic.Field(
        None,
        description="",
    )
    badges: typing.Optional["KworkBadges"] = pydantic.Field(
        None,
        description="",
    )


class CancelReason(pydantic.BaseModel):
    id: typing.Optional[str] = pydantic.Field(
        None,
        description="Идентификатор причины",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Наименование причины",
    )
    commentRequired: typing.Optional[bool] = pydantic.Field(
        None,
        description="Возможность добавлять комментарии",
    )
    subtypes: typing.Optional[typing.List[dict]] = pydantic.Field(
        None,
        description="Достпуные дочерние причины отмены",
    )


class InboxMessage(pydantic.BaseModel):
    message_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID сообщений",
    )
    to_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID получаетеля",
    )
    to_username: typing.Optional[str] = pydantic.Field(
        None,
        description="Username получателя",
    )
    to_live_date: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата последней активности получателя на сайте UNIXTIME",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор пользователя отправителя",
    )
    from_username: typing.Optional[str] = pydantic.Field(
        None,
        description="Имя пользователя отправителя",
    )
    from_live_date: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата последней активности отправителя на сайте UNIXTIME",
    )
    from_profilepicture: typing.Optional[str] = pydantic.Field(
        None,
        description="Ссылка на аватар отправителя",
    )
    to_profilepicture: typing.Optional[str] = pydantic.Field(
        None,
        description="Ссылка на аватар получателя",
    )
    message: typing.Optional[str] = pydantic.Field(
        None,
        description="Текст сообщения. Возможен HTML",
    )
    time: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата сообщения UNIXTIME",
    )
    unread: typing.Optional[bool] = pydantic.Field(
        None,
        description="Сообщение непрочитано",
    )
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="""Тип сообщения: NULL - обычное сообщение,
	 * 					custom_request - Запрос на индивидуальный кворк, offer_kwork_new - Предложение кворка,
	 *     				offer_kwork_payer_cancel - Предложение индивидуального кворка отклонено покупателем,
	 *     				offer_kwork_worker_cancel - Предложение индивидуального кворка отклонено продавцом,
	 *     				offer_kwork_done - Заказ создан, auto - Автоуведомление, support - Сообщение от техподдержки,
	 *     				report - Жалоба на пользователя""",
    )
    status: typing.Optional[str] = pydantic.Field(
        None,
        description="Заглушка после удаления поля 'status'",
    )
    created_order_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Id созданного заказа индивидуального предложения",
    )
    forwarded: typing.Optional[bool] = pydantic.Field(
        None,
        description="Флаг является ли сообщение пересланным",
    )
    updated_at: typing.Optional[int] = pydantic.Field(
        None,
        description="Время изменения сообщения в Unixtime, или null",
    )
    warning_type: typing.Optional[str] = pydantic.Field(
        None,
        description="""флаги для получение статуса игнорирования сообщения
	 * 					(check — постановка сообщения на проверку, answer — на сообщение был ответ, ignore — сообщение было проигнорировано)""",
    )
    countup: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество часов до ответа, -1 - значение не задано",
    )
    files: typing.Optional[typing.List["FileWithMiniature"]] = pydantic.Field(
        None,
        description="файлы сообщения",
    )
    quote: typing.Optional[dict] = pydantic.Field(
        None,
        description="Цитируемое сообщение",
    )
    message_page: typing.Optional[int] = pydantic.Field(
        None,
        description="Страница на которой находится сообщение",
    )
    custom_request: typing.Optional[dict] = pydantic.Field(
        None,
        description="Запрос на индивидуальный кворк",
    )
    inbox_order: typing.Optional["InboxOrder"] = pydantic.Field(
        None,
        description="",
    )


class InboxTrackMessage(pydantic.BaseModel):
    conversation_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID сообщений в conversation",
    )
    message_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID сообщений в Inbox/Track",
    )
    entity_type: typing.Optional[int] = pydantic.Field(
        None,
        description="Тип сообщения (9 - Inbox, 10 - Track",
    )
    to_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID получаетеля",
    )
    to_username: typing.Optional[str] = pydantic.Field(
        None,
        description="Username получателя",
    )
    to_live_date: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата последней активности получателя на сайте UNIXTIME",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор пользователя отправителя",
    )
    from_username: typing.Optional[str] = pydantic.Field(
        None,
        description="Имя пользователя отправителя",
    )
    from_live_date: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата последней активности отправителя на сайте UNIXTIME",
    )
    from_profilepicture: typing.Optional[str] = pydantic.Field(
        None,
        description="Ссылка на аватар отправителя",
    )
    to_profilepicture: typing.Optional[str] = pydantic.Field(
        None,
        description="Ссылка на аватар получателя",
    )
    forwarder_from_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор пользователя, от которого переслано сообщение",
    )
    forwarded_from_username: typing.Optional[str] = pydantic.Field(
        None,
        description="Имя пользователя, от которого переслано сообщение",
    )
    message: typing.Optional[str] = pydantic.Field(
        None,
        description="Текст сообщения. Возможен HTML",
    )
    time: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата сообщения UNIXTIME",
    )
    unread: typing.Optional[bool] = pydantic.Field(
        None,
        description="Сообщение непрочитано",
    )
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="Тип сообщения: NULL - обычное сообщение, custom_request - Запрос на индивидуальный кворк, offer_kwork_new - Предложение кворка, offer_kwork_payer_cancel - Предложение индивидуального кворка отклонено покупателем, offer_kwork_worker_cancel - Предложение индивидуального кворка отклонено продавцом, offer_kwork_done - Заказ создан, auto - Автоуведомление, support - Сообщение от техподдержки, report - Жалоба на пользователя",
    )
    status: typing.Optional[str] = pydantic.Field(
        None,
        description="Заглушка после удаления поля 'status'",
    )
    created_order_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Id созданного заказа индивидуального предложения",
    )
    forwarded: typing.Optional[bool] = pydantic.Field(
        None,
        description="Флаг является ли сообщение пересланным",
    )
    updated_at: typing.Optional[int] = pydantic.Field(
        None,
        description="Время изменения сообщения в Unixtime, или null",
    )
    warning_type: typing.Optional[str] = pydantic.Field(
        None,
        description="флаги для получение статуса игнорирования сообщения (check — постановка сообщения на проверку, answer — на сообщение был ответ, ignore — сообщение было проигнорировано)",
    )
    countup: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество часов до ответа, -1 - значение не задано",
    )
    files: typing.Optional[typing.List["FileWithMiniature"]] = pydantic.Field(
        None,
        description="файлы сообщения",
    )
    quote: typing.Optional[dict] = pydantic.Field(
        None,
        description="Цитируемое сообщение",
    )
    message_page: typing.Optional[int] = pydantic.Field(
        None,
        description="Страница на которой находится сообщение",
    )
    custom_request: typing.Optional[dict] = pydantic.Field(
        None,
        description="Запрос на индивидуальный кворк",
    )
    inbox_order: typing.Optional["InboxOrder"] = pydantic.Field(
        None,
        description="",
    )
    track_order: typing.Optional["TrackOrder"] = pydantic.Field(
        None,
        description="",
    )


class OrderDetails(pydantic.BaseModel):
    details: typing.Optional[dict] = pydantic.Field(
        None,
        description="Детали заказа",
    )
    stages: typing.Optional[typing.List[dict]] = pydantic.Field(
        None,
        description="Этапы заказа",
    )
    key_tracks: typing.Optional[typing.List[dict]] = pydantic.Field(
        None,
        description="Треки заказа",
    )


class OrderOption(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор опции",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Наименование опции",
    )
    price: typing.Optional[int] = pydantic.Field(
        None,
        description="Стоимость опции",
    )
    currency: typing.Optional[str] = pydantic.Field(
        None,
        description="Валюта опции",
    )
    time: typing.Optional[int] = pydantic.Field(
        None,
        description="Добавочная длительность к заказу",
    )


class FirstLevelCategory(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор рубрики",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Название рубрики",
    )
    rubric_description: typing.Optional[str] = pydantic.Field(
        None,
        description="Описание",
    )
    ico: typing.Optional[str] = pydantic.Field(
        None,
        description="Иконка",
    )
    ico_extra: typing.Optional[str] = pydantic.Field(
        None,
        description="Иконка png",
    )
    order: typing.Optional[int] = pydantic.Field(
        None,
        description="Порядок сортировки",
    )
    category_image: typing.Optional[str] = pydantic.Field(
        None,
        description="Путь к изображению",
    )


class SecondLevelCategory(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор рубрики",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Название рубрики",
    )
    rubric_description: typing.Optional[str] = pydantic.Field(
        None,
        description="Описание",
    )
    order: typing.Optional[int] = pydantic.Field(
        None,
        description="Порядок сортировки",
    )
    category_image: typing.Optional[str] = pydantic.Field(
        None,
        description="Путь к изображению",
    )
    kworks_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество кворков",
    )


class PopularBlockCategories(pydantic.BaseModel):
    category_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор категории, может быть null если это классификация",
    )
    classifier_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор классификации, может быть null если это категория",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Название рубрики",
    )
    order: typing.Optional[int] = pydantic.Field(
        None,
        description="Порядок сортировки",
    )
    cover_url: typing.Optional[str] = pydantic.Field(
        None,
        description="Путь к изображению",
    )
    kworks_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество кворков",
    )


class PopularBlock(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Наименование блока",
    )
    block_description: typing.Optional[str] = pydantic.Field(
        None,
        description="Описание блока",
    )
    categories: typing.Optional[typing.List["PopularBlockCategories"]] = pydantic.Field(
        None,
        description="Массив категорий",
    )
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID категории",
    )
    order: typing.Optional[int] = pydantic.Field(
        None,
        description="Порядок",
    )


class CatalogServiceBlock(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор категории",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Наименование",
    )
    rubric_description: typing.Optional[str] = pydantic.Field(
        None,
        description="Описание рубрики(основные категории)",
    )
    icon_path: typing.Optional[str] = pydantic.Field(
        None,
        description="Иконка рубрики",
    )
    order: typing.Optional[int] = pydantic.Field(
        None,
        description="Порядок сортировки",
    )


class CatalogOtherServiceBlock(pydantic.BaseModel):
    category_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор категории, может быть null если это классификация",
    )
    classifier_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор классификации, может быть null если это категория",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Название рубрики",
    )
    order: typing.Optional[int] = pydantic.Field(
        None,
        description="Порядок сортировки",
    )
    cover_url: typing.Optional[str] = pydantic.Field(
        None,
        description="Путь к изображению",
    )


class NotificationType(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Название",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Описание",
    )
    is_red: typing.Optional[bool] = pydantic.Field(
        None,
        description="Важное ли",
    )
    priority: typing.Optional[int] = pydantic.Field(
        None,
        description="Приоритет",
    )
    entity_type: typing.Optional[str] = pydantic.Field(
        None,
        description="Тип связанной сущности",
    )
    notifications: typing.Optional[typing.List["Notification"]] = pydantic.Field(
        None,
        description="Уведомления данного типа",
    )


class SimpleNotification(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор",
    )
    added: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата создания unixtime",
    )
    entity_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор связанной сущности",
    )
    link: typing.Optional[str] = pydantic.Field(
        None,
        description="Ссылка для перехода",
    )


class PushEvent(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор сквозной очереди непрочитанных push-событий",
    )
    entity_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор сущности, связанной с push-событием (inbox_id, notity_id",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор пользователя-получателя (текущий)",
    )
    data: typing.Optional[dict] = pydantic.Field(
        None,
        description="Данные push-события (свой набор для каждой сущности)",
    )
    created_at: typing.Optional[str] = pydantic.Field(
        None,
        description="Дата создания события",
    )
    event: typing.Optional[str] = pydantic.Field(
        None,
        description="Наименование события",
    )


class Offer(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор предложения",
    )
    status: typing.Optional[str] = pydantic.Field(
        None,
        description="Статус предложения",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Название предложения",
    )
    comment: typing.Optional[str] = pydantic.Field(
        None,
        description="Комментарий к предложению",
    )
    price: typing.Optional[int] = pydantic.Field(
        None,
        description="Цена предложения",
    )
    duration: typing.Optional[int] = pydantic.Field(
        None,
        description="Срок выполнения дней",
    )
    date_create: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата создания предложения",
    )
    is_actual: typing.Optional[bool] = pydantic.Field(
        None,
        description="Флаг актуальности предложения",
    )
    is_read: typing.Optional[bool] = pydantic.Field(
        None,
        description="Флаг прочитанности предложения покупателем",
    )
    want_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор запроса на услугу",
    )
    order_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор заказа",
    )
    kwork_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор кворка",
    )
    project: typing.Optional["WantWorker"] = pydantic.Field(
        None,
        description="",
    )


class OrderHeader(pydantic.BaseModel):
    order: typing.Optional[dict] = pydantic.Field(
        None,
        description="Данные заказа",
    )
    kwork: typing.Optional[dict] = pydantic.Field(
        None,
        description="Данные кворка",
    )
    worker: typing.Optional[dict] = pydantic.Field(
        None,
        description="Данные продавца",
    )
    payer: typing.Optional[dict] = pydantic.Field(
        None,
        description="Данные покупателя",
    )


class OrderedExtra(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID опции",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Название опции",
    )
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество заказанных опций",
    )
    payer_price: typing.Optional[int] = pydantic.Field(
        None,
        description="Цена заказанных опции для покупателя",
    )
    worker_price: typing.Optional[int] = pydantic.Field(
        None,
        description="Цена заказанных опции для продавца",
    )
    totaldays: typing.Optional[int] = pydantic.Field(
        None,
        description="Общая длительность в днях",
    )


class Interlocutor(pydantic.BaseModel):
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор пользователя",
    )
    username: typing.Optional[str] = pydantic.Field(
        None,
        description="Имя пользователя",
    )
    last_online_timestamp: typing.Optional[int] = pydantic.Field(
        None,
        description="Последнее время в сети (unixtime)",
    )
    avatar_image_path: typing.Optional[str] = pydantic.Field(
        None,
        description="Абсолютный урл аватара",
    )


class Package(pydantic.BaseModel):
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Описание пакета",
    )
    price: typing.Optional[int] = pydantic.Field(
        None,
        description="Цена пакета",
    )
    duration: typing.Optional[int] = pydantic.Field(
        None,
        description="Продолжительность в днях",
    )
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="Тип пакета",
    )
    items: typing.Optional[typing.List["PackageItem"]] = pydantic.Field(
        None,
        description="Массив опций пакета",
    )


class PackageItem(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор опции пакета",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Название опции",
    )
    value: typing.Optional[str] = pydantic.Field(
        None,
        description="Значение опции",
    )
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="Тип значения опции",
    )
    name_1: typing.Optional[str] = pydantic.Field(
        None,
        description="Название опции в единственном числе",
    )
    name_2: typing.Optional[str] = pydantic.Field(
        None,
        description="Название опции для 2",
    )
    name_5: typing.Optional[str] = pydantic.Field(
        None,
        description="Название опции для 5",
    )


class Error(pydantic.BaseModel):
    success: typing.Optional[bool] = pydantic.Field(
        None,
        description="Флаг успешности",
    )
    error: typing.Optional[str] = pydantic.Field(
        None,
        description="Текст ошибки",
    )
    error_code: typing.Optional[int] = pydantic.Field(
        None,
        description="Код ошибки",
    )


class Paging(pydantic.BaseModel):
    page: typing.Optional[int] = pydantic.Field(
        None,
        description="Текущая страница",
    )
    total: typing.Optional[int] = pydantic.Field(
        None,
        description="Общее количество элементов",
    )
    limit: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество элементов на странице",
    )


class ProfileKwork(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор",
    )
    category_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID категории",
    )
    category_name: typing.Optional[str] = pydantic.Field(
        None,
        description="Название категории",
    )
    classification_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID атрибута-значения классификации верхнего уровня",
    )
    status_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор статуса кворка",
    )
    status_name: typing.Optional[str] = pydantic.Field(
        None,
        description="Название статуса",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Название кворка",
    )
    image_url: typing.Optional[str] = pydantic.Field(
        None,
        description="Относительный путь к обложке кворка",
    )
    price: typing.Optional[int] = pydantic.Field(
        None,
        description="Стоимость кворка",
    )
    is_price_from: typing.Optional[bool] = pydantic.Field(
        None,
        description="Необходима ли подпись 'Цена ОТ'",
    )
    is_best: typing.Optional[bool] = pydantic.Field(
        None,
        description="Кворк имеет высший рейтинг",
    )
    is_hidden: typing.Optional[bool] = pydantic.Field(
        None,
        description="Кворк скрыт у активного юзера",
    )
    is_favorite: typing.Optional[bool] = pydantic.Field(
        None,
        description="Кворк в избранных у активного юзера",
    )
    is_viewed: typing.Optional[bool] = pydantic.Field(
        None,
        description="Просмотрен ли кворк",
    )
    isSubscription: typing.Optional[bool] = pydantic.Field(
        None,
        description="Кворк с подпиской?",
    )
    lang: typing.Optional[str] = pydantic.Field(
        None,
        description="Язык кворка, для привзяки валюты",
    )
    order: typing.Optional[int] = pydantic.Field(
        None,
        description="Порядок вывода в списке",
    )
    worker: typing.Optional["UserWorker"] = pydantic.Field(
        None,
        description="",
    )
    edits_list: typing.Optional[typing.List[str]] = pydantic.Field(
        None,
        description="Массив строк что нужно исправить в кворке, для текущего юзера",
    )
    activity: typing.Optional[dict] = pydantic.Field(
        None,
        description="Активность для текущего юзера",
    )
    badges: typing.Optional["KworkBadges"] = pydantic.Field(
        None,
        description="",
    )


class Resize(pydantic.BaseModel):
    x: typing.Optional[int] = pydantic.Field(
        None,
        description="Сдвиг по вертикали в % от ширины оригинального изображения",
    )
    y: typing.Optional[int] = pydantic.Field(
        None,
        description="Сдвиг по горизонтали в % от высоты оригинального изображения",
    )
    w: typing.Optional[int] = pydantic.Field(
        None,
        description="Ширина в % от ширины оригинального изображения",
    )
    h: typing.Optional[int] = pydantic.Field(
        None,
        description="Высота в % от ширины оригинального изображения",
    )


class User(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор пользователя",
    )
    username: typing.Optional[str] = pydantic.Field(
        None,
        description="Имя пользователя",
    )
    profilepicture: typing.Optional[str] = pydantic.Field(
        None,
        description="Путь к изображению аватара",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Текст о себе",
    )
    slogan: typing.Optional[str] = pydantic.Field(
        None,
        description="Слоган - не заполнен",
    )
    fullname: typing.Optional[str] = pydantic.Field(
        None,
        description="Настоящее имя",
    )
    level_description: typing.Optional[str] = pydantic.Field(
        None,
        description="Название уровня продавца",
    )
    cover: typing.Optional[str] = pydantic.Field(
        None,
        description="Путь к баннеру пользователя",
    )
    good_reviews: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество положительных отзывов",
    )
    bad_reviews: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество отрицательных отзывов",
    )
    reviews_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Общее количество отзывов",
    )
    location: typing.Optional[str] = pydantic.Field(
        None,
        description="Город или страна",
    )
    rating: typing.Optional[str] = pydantic.Field(
        None,
        description="Рейтинг по 5 бальной шкале с 1 десятичным знаком",
    )
    rating_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество отзывов",
    )
    online: typing.Optional[bool] = pydantic.Field(
        None,
        description="Онлайн ли пользователь",
    )
    live_date: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата последней активности на сайте",
    )
    custom_request_min_budget: typing.Optional[int] = pydantic.Field(
        None,
        description="Минимальный бюджет запроса на индивидуальный кворк (представлен только в случае если пользователь авторизован)",
    )
    is_allow_custom_request: typing.Optional[bool] = pydantic.Field(
        None,
        description="Принимает ли пользователь запросы на индивидуальные кворки",
    )
    order_done_persent: typing.Optional[int] = pydantic.Field(
        None,
        description="Процент успешно сданных заказов",
    )
    order_done_intime_persent: typing.Optional[int] = pydantic.Field(
        None,
        description="Процент сданных вовремя заказов",
    )
    order_done_repeat_persent: typing.Optional[int] = pydantic.Field(
        None,
        description="Процент повторных заказов",
    )
    timezoneId: typing.Optional[int] = pydantic.Field(
        None,
        description="id временной зоны",
    )
    blocked_by_user: typing.Optional[bool] = pydantic.Field(
        None,
        description="Заблокирован ли диалог с пользователем (всегда false если запрос от неавторизованного пользователя)",
    )
    allowedDialog: typing.Optional[bool] = pydantic.Field(
        None,
        description="Разрешено ли писать пользователю",
    )
    addtime: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата регистрации",
    )
    achievments_list: typing.List[typing.Optional["ProfileBadges"]] = pydantic.Field(
        None,
        description="",
    )
    completed_orders_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество выполненных заказов",
    )
    profession: typing.Optional[str] = pydantic.Field(
        None,
        description="Специальность пользователя",
    )
    kworks_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество активных кворков",
    )
    kworks: typing.Optional["ProfileKworks"] = pydantic.Field(
        None,
        description="",
    )
    portfolio_list: typing.Optional["ProfilePortfolios"] = pydantic.Field(
        None,
        description="",
    )
    reviews: typing.Optional[typing.List["UserReview"]] = pydantic.Field(
        None,
        description="Массив отзывов",
    )


class FavouriteCategory(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID категории",
    )
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Название категории",
    )


class UserReview(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор отзыва. Может быть NULL если это портфолио",
    )
    time_added: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата добавления отзыва или портфолио UNIXTIME",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Текст отзыва. Может быть NULL если это портфолио",
    )
    auto_mode: typing.Optional[str] = pydantic.Field(
        None,
        description="Статус автоматического создания отзыва: inwork_time_over - Просрочено время взятия в работу, time_over - Просрочено время выполнения, incorrect_execute - Некорректное выполнение",
    )
    good: typing.Optional[bool] = pydantic.Field(
        None,
        description="Является ли отзыв положительным",
    )
    bad: typing.Optional[bool] = pydantic.Field(
        None,
        description="Является ли отзыв отрицательным",
    )
    kwork: typing.Optional[dict] = pydantic.Field(
        None,
        description="Объект кворка",
    )
    writer: typing.Optional["UserReviewWriter"] = pydantic.Field(
        None,
        description="",
    )
    answer: typing.Optional["UserAnswer"] = pydantic.Field(
        None,
        description="",
    )
    portfolio: typing.Optional["Portfolio"] = pydantic.Field(
        None,
        description="",
    )


class Versions(pydantic.BaseModel):
    current_version_ios: typing.Optional[str] = pydantic.Field(
        None,
        description="Текущая версия iOS",
    )
    current_version_android: typing.Optional[str] = pydantic.Field(
        None,
        description="Текущая версия Android",
    )
    critical_update: typing.Optional[bool] = pydantic.Field(
        None,
        description="Обязательное обновление или рекомендуемое",
    )
    facebook: typing.Optional[bool] = pydantic.Field(
        None,
        description="Можно ли отображать facebook",
    )


class WantPayer(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор проекта",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Заголовок проекта",
    )
    description: typing.Optional[str] = pydantic.Field(
        None,
        description="Описание проекта",
    )
    status: typing.Optional[str] = pydantic.Field(
        None,
        description="Статус проекта",
    )
    want_status_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор статуса (альтернативный статус)",
    )
    date_create: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата создания проекта",
    )
    date_active: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата активации проекта",
    )
    date_expire: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата окончания проекта",
    )
    date_reject: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата отклонения проекта",
    )
    price_limit: typing.Optional[int] = pydantic.Field(
        None,
        description="Бюджет проекта",
    )
    views: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество просмотров",
    )
    orders: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество заказов по проекту",
    )
    offers: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество предложений по проекту",
    )
    views_history: typing.Optional[dict] = pydantic.Field(
        None,
        description="Массив количества просмотров, сгруппированный по дням",
    )
    category_base_price: typing.Optional[int] = pydantic.Field(
        None,
        description="Базовая стоимость работ в категории запроса",
    )
    allow_higher_price: typing.Optional[bool] = pydantic.Field(
        None,
        description="Готов ли покупатель рассмотреть предложения с ценой выше",
    )
    possible_price_limit: typing.Optional[int] = pydantic.Field(
        None,
        description="Лимит цены предложений с учетом готовности покупателя рассмотреть предложения с ценой выше",
    )


class WantsList(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор статуса",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Отображаемое название статуса",
    )
    tootlip: typing.Optional[str] = pydantic.Field(
        None,
        description="Описание статуса",
    )
    order: typing.Optional[int] = pydantic.Field(
        None,
        description="Порядковый номер вкладки",
    )
    projects_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество запросов на услугу в статусе",
    )
    wants: typing.Optional[typing.List["WantPayer"]] = pydantic.Field(
        None,
        description="Список заявок на услугу",
    )


class ExchangeInfo(pydantic.BaseModel):
    exchange_response_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество моих откликов на бирже",
    )
    archived_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество заархивированных проектов",
    )


class Connects(pydantic.BaseModel):
    all_connects: typing.Optional[int] = pydantic.Field(
        None,
        description="Кол-во коннектов продавца",
    )
    active_connects: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество доступных коннектов",
    )
    update_time: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата начисления коннектов (UNIX), -1 - дата начисления не определена (выводится как Н/Д)",
    )


class BudgetWithCount(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(
        None,
        description="Наименование диапазона",
    )
    boundaries: typing.Optional[dict] = pydantic.Field(
        None,
        description="Диапазон цен",
    )
    count: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество проектов в диапазоне",
    )


class WantsFilter(pydantic.BaseModel):
    categories: typing.Optional[typing.List["FavouriteCategory"]] = pydantic.Field(
        None,
        description="Массив объектов рубрик",
    )
    price_from: typing.Optional[int] = pydantic.Field(
        None,
        description="Бюджет от (не обязательно)",
    )
    price_to: typing.Optional[int] = pydantic.Field(
        None,
        description="Бюджет до (не обязательно)",
    )
    hiring_to: typing.Optional[int] = pydantic.Field(
        None,
        description="Процент найма от (не обязательно)",
    )
    kworks_filter_from: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество предложений от (не обязательно)",
    )
    kworks_filter_to: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество предложений до (не обязательно)",
    )


class Attribute(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор",
    )
    title: typing.Optional[str] = pydantic.Field(
        None,
        description="Название",
    )
    lang: typing.Optional[str] = pydantic.Field(
        None,
        description="Язык",
    )
    h1: typing.Optional[str] = pydantic.Field(
        None,
        description="Seo заголовок страницы",
    )
    hint_payer: typing.Optional[str] = pydantic.Field(
        None,
        description="Подсказка для покупателя",
    )
    hint_worker: typing.Optional[str] = pydantic.Field(
        None,
        description="Подсказка для продавца",
    )
    note_worker: typing.Optional[str] = pydantic.Field(
        None,
        description="Комментарий для продавца",
    )
    category_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор категории",
    )
    visible: typing.Optional[int] = pydantic.Field(
        None,
        description="Видимость",
    )
    is_classification: typing.Optional[bool] = pydantic.Field(
        None,
        description="Является классификацией",
    )
    required: typing.Optional[bool] = pydantic.Field(
        None,
        description="Обязателен выбор потомков при редактировании",
    )
    allow_multiple: typing.Optional[bool] = pydantic.Field(
        None,
        description="Разрешен множественный выбор потомков",
    )
    multiple_max_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Максимальное количество выбранных потомков",
    )
    allow_custom: typing.Optional[bool] = pydantic.Field(
        None,
        description="Разрешено добавление пользовательских потомков",
    )
    portfolio: typing.Optional[bool] = pydantic.Field(
        None,
        description="Отображать портфолио на странице мои портфолио",
    )
    parent_portfolio: typing.Optional[bool] = pydantic.Field(
        None,
        description="Отображать портфолио на странице мои портфолио (унаследовано)",
    )
    is_custom: typing.Optional[bool] = pydantic.Field(
        None,
        description="Пользовательский",
    )
    custom_max_count: typing.Optional[bool] = pydantic.Field(
        None,
        description="Максимальное количество пользовательских потомков",
    )
    demo_file_upload: typing.Optional[bool] = pydantic.Field(
        None,
        description="Разрешена загрузка демо-отчета",
    )
    custom_moderation_status: typing.Optional[str] = pydantic.Field(
        None,
        description="Статус модерации пользовательского",
    )
    order_index: typing.Optional[int] = pydantic.Field(
        None,
        description="Приоритет сортировки",
    )
    is_free_price: typing.Optional[bool] = pydantic.Field(
        None,
        description="Свободная цена",
    )
    unembedded: typing.Optional[bool] = pydantic.Field(
        None,
        description="Отображать невложенным в основное дерево",
    )
    percent_usage: typing.Optional[str] = pydantic.Field(
        None,
        description="Процент использования в кворках",
    )
    portfolio_type: typing.Optional[str] = pydantic.Field(
        None,
        description="Разрешено портфолио",
    )
    orders_inprogress_limit: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество заказов кворка, при котором он становится на паузу",
    )
    orders_inprogress_pause_off: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество заказов кворка, при котором он снимается с паузы",
    )
    depth: typing.Optional[int] = pydantic.Field(
        None,
        description="Глубина в дереве",
    )
    is_custom_extra_denied: typing.Optional[bool] = pydantic.Field(
        None,
        description="Запрещено добавлять пакетные доп.опции в кворке",
    )
    is_subscribe_price: typing.Optional[bool] = pydantic.Field(
        None,
        description="Цена по подписке",
    )
    is_kwork_links_sites: typing.Optional[int] = pydantic.Field(
        None,
        description="Необходимость предоставления списка ссылок - 1, доменов - 2, сайтов - 3",
    )
    meta_title: typing.Optional[str] = pydantic.Field(
        None,
        description="Значение для meta тега title",
    )
    meta_description: typing.Optional[str] = pydantic.Field(
        None,
        description="Значение для meta тега description",
    )
    parent_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор родителя",
    )
    volume_type_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор числового объема",
    )
    base_volume: typing.Optional[int] = pydantic.Field(
        None,
        description="Базовый числовой объем",
    )
    min_volume: typing.Optional[int] = pydantic.Field(
        None,
        description="Минимальный числовой объем",
    )
    max_volume: typing.Optional[int] = pydantic.Field(
        None,
        description="Максимальный числовой объем",
    )
    min_volume_type_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор типа минимального числовой объема",
    )
    max_volume_type_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор типа максимального числовой объема",
    )
    custom_descendant_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество пользовательских атрибутов среди потомков",
    )
    kworks_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество активных кворков в которых используется атрибут",
    )
    alias: typing.Optional[str] = pydantic.Field(
        None,
        description="Алиас в каталоге",
    )
    duplicated_attribute_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор дублируемого атрибута",
    )
    twin_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор атрибута близнеца в другом языке",
    )
    is_smm_hide: typing.Optional[bool] = pydantic.Field(
        None,
        description="Является ли скрываемым по логике SMM",
    )
    children: typing.Optional[typing.List["Attribute"]] = pydantic.Field(
        None,
        description="Потомки",
    )


class Attributes(pydantic.BaseModel):
    pass


class TrackFile(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор файла",
    )
    name: typing.Optional[int] = pydantic.Field(
        None,
        description="Имя файла",
    )
    file_url: typing.Optional[str] = pydantic.Field(
        None,
        description="Абсолютный урл файла на сервере",
    )
    miniature_url: typing.Optional[str] = pydantic.Field(
        None,
        description="Абсолютный урл миниатюры",
    )
    size_in_bytes: typing.Optional[int] = pydantic.Field(
        None,
        description="Размер файла в байтах",
    )


class Track(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор сообщения",
    )
    sent_timestamp: typing.Optional[int] = pydantic.Field(
        None,
        description="Время отправки UnixTime",
    )
    text: typing.Optional[str] = pydantic.Field(
        None,
        description="Текст сообщения",
    )
    from_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор отправителя",
    )
    from_name: typing.Optional[str] = pydantic.Field(
        None,
        description="Имя отправителя",
    )
    files: typing.Optional[typing.List["TrackFile"]] = pydantic.Field(
        None,
        description="Данные об изображениях",
    )
    is_unread: typing.Optional[bool] = pydantic.Field(
        None,
        description="Прочитано ли сообщение",
    )
    updated_at: typing.Optional[int] = pydantic.Field(
        None,
        description="Время изменения сообщения, UnixTime",
    )
    quote: typing.Optional["TrackQuote"] = pydantic.Field(
        None,
        description="",
    )
    type: typing.Optional[int] = pydantic.Field(
        None,
        description="Тип сообщения",
    )


class ParentCategory(Category):
    subcategories: typing.Optional[typing.List["Category"]] = pydantic.Field(
        None,
        description="Подкатегории",
    )


class DialogMessage(pydantic.BaseModel):
    unread_count: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество непрочитанных сообщений",
    )
    last_message: typing.Optional[str] = pydantic.Field(
        None,
        description="Текст последнего сообщения",
    )
    time: typing.Optional[int] = pydantic.Field(
        None,
        description="Время последнего сообщения UNIXTIME",
    )
    user_id: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор пользователя-собеседника",
    )
    username: typing.Optional[str] = pydantic.Field(
        None,
        description="Имя пользователя - собеседника",
    )
    profilepicture: typing.Optional[str] = pydantic.Field(
        None,
        description="Ссылка на аватар пользователя - собеседника",
    )
    is_online: typing.Optional[bool] = pydantic.Field(
        None,
        description="Онлайн ли собеседник",
    )
    lastOnlineTime: typing.Optional[int] = pydantic.Field(
        None,
        description="Время, когда пользователь был последний раз онлайн",
    )
    link: typing.Optional[str] = pydantic.Field(
        None,
        description="Ссылка страницы, на которую должен попадать пользователь",
    )
    status: typing.Optional[str] = pydantic.Field(
        None,
        description="Заглушка после удаления поля 'status'",
    )
    blocked_by_user: typing.Optional[bool] = pydantic.Field(
        None,
        description="Заблокирован ли диалог с пользователем - собеседником",
    )
    allowedDialog: typing.Optional[bool] = pydantic.Field(
        None,
        description="Разрешено ли писать пользователю - собеседнику",
    )
    lastMessage: typing.Optional["DialogLastMessage"] = pydantic.Field(
        None,
        description="",
    )
    has_active_order: typing.Optional[bool] = pydantic.Field(
        None,
        description="Есть ли активный заказ среди собеседников",
    )
    archived: typing.Optional[bool] = pydantic.Field(
        None,
        description="Является ли диалог архивным или нет",
    )
    isStarred: typing.Optional[bool] = pydantic.Field(
        None,
        description="Помечен ли диалог как избранный",
    )
    warning_message_id: typing.Optional[int] = pydantic.Field(
        None,
        description="id сообщения на которое требуется обязательный ответ",
    )
    countup: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество часов до ответа, -1 - значение не задано",
    )
    has_answer: typing.Optional[bool] = pydantic.Field(
        None,
        description="Был ли ответ в диалоге пользователей",
    )
    is_allow_custom_request: typing.Optional[bool] = pydantic.Field(
        None,
        description="Принимает ли пользователь запросы на индивидуальный кворк",
    )
    hidden_at: typing.Optional[int] = pydantic.Field(
        None,
        description="Время скрытия/удаления диалога",
    )
    disallowReason: typing.Optional[int] = pydantic.Field(
        None,
        description="Причина невозможности ведения диалога",
    )


class FileWithSize(File):
    size: typing.Optional[int] = pydantic.Field(
        None,
        description="Размер в байтах",
    )
    timestamp: typing.Optional[int] = pydantic.Field(
        None,
        description="Дата создания",
    )
    status: typing.Optional[str] = pydantic.Field(
        None,
        description="Статус",
    )


class FileWithMiniature(FileWithSize):
    miniature_url: typing.Optional[str] = pydantic.Field(
        None,
        description="Ссылка на файл с миниатюрой",
    )
    miniature_path: typing.Optional[str] = pydantic.Field(
        None,
        description="Путь к файлу миниатюры",
    )
    imageData: typing.Optional[dict] = pydantic.Field(
        None,
        description="Данные низкокачественного изображения",
    )


class GetMessage(InboxMessage):
    page: typing.Optional[int] = pydantic.Field(
        None,
        description="Номер страницы где находится сообщение",
    )


class GetMessageWithTrack(InboxTrackMessage):
    page: typing.Optional[int] = pydantic.Field(
        None,
        description="Номер страницы где находится сообщение",
    )


class UserNotification(SimpleNotification):
    otherUserId: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор другого пользователя",
    )
    otherUserName: typing.Optional[str] = pydantic.Field(
        None,
        description="Имя другого пользователя",
    )
    otherUserAvatar: typing.Optional[str] = pydantic.Field(
        None,
        description="Ссылка на изображение аватара другого пользователя",
    )
    isOtherUserOnline: typing.Optional[bool] = pydantic.Field(
        None,
        description="Онлайн ли другой пользователь",
    )


class OrderNotification(UserNotification):
    orderId: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор заказа",
    )
    orderTitle: typing.Optional[str] = pydantic.Field(
        None,
        description="Название заказа",
    )


class StageNotification(OrderNotification):
    stageTitle: typing.Optional[str] = pydantic.Field(
        None,
        description="Название этапа",
    )


class KworkNotification(SimpleNotification):
    kworkTitle: typing.Optional[str] = pydantic.Field(
        None,
        description="Название кворка",
    )


class Notification(
    KworkNotification,
    StageNotification,
):
    pass


class KworkFile(FileWithSize):
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="Тип файла: kwork_description - Файл для описания кворка, kwork_instruction - Файл для инструкции",
    )


class PackageWithUpgrade(Package):
    upgrade: typing.Optional["Package"] = pydantic.Field(
        None,
        description="",
    )


class PagingWithPages(Paging):
    pages: typing.Optional[int] = pydantic.Field(
        None,
        description="Количество страниц",
    )


class FavoriteKworks(ProfileKwork):
    classifier_id: typing.Optional[int] = pydantic.Field(
        None,
        description="ID последнего атрибута/классификации",
    )


class DialogLastMessage(pydantic.BaseModel):
    unread: typing.Optional[bool] = pydantic.Field(
        None,
        description="Было ли прочитано последнне сообщение",
    )
    fromUsername: typing.Optional[str] = pydantic.Field(
        None,
        description="Имя пользователя который отправил последнее сообщение",
    )
    fromUserId: typing.Optional[int] = pydantic.Field(
        None,
        description="Идентификатор пользователя который отправил последнее сообщение",
    )
    type: typing.Optional[str] = pydantic.Field(
        None,
        description="Тип посленего соощения",
    )
    time: typing.Optional[int] = pydantic.Field(
        None,
        description="Время отправки последнего сообщения",
    )
    message: typing.Optional[str] = pydantic.Field(
        None,
        description="Текст последнего сообщения",
    )
    profilePicture: typing.Optional[str] = pydantic.Field(
        None,
        description="URL аватара профайла пользователя",
    )


Achievements.update_forward_refs()
KworkBadges.update_forward_refs()
InboxOrder.update_forward_refs()
TrackOrder.update_forward_refs()
Portfolio.update_forward_refs()
ProfilePortfolios.update_forward_refs()
UserAnswer.update_forward_refs()
ProfileKworks.update_forward_refs()
UserWorker.update_forward_refs()
ProfileBadges.update_forward_refs()
UserReviewWriter.update_forward_refs()
WantWorker.update_forward_refs()
TrackQuote.update_forward_refs()
Achievement.update_forward_refs()
VolumeType.update_forward_refs()
PositiveReviewsCount.update_forward_refs()
Category.update_forward_refs()
ComplainCategory.update_forward_refs()
KworkLinkSiteItem.update_forward_refs()
File.update_forward_refs()
ShortUserInfo.update_forward_refs()
KworkPackage.update_forward_refs()
KworkInList.update_forward_refs()
CancelReason.update_forward_refs()
InboxMessage.update_forward_refs()
InboxTrackMessage.update_forward_refs()
OrderDetails.update_forward_refs()
OrderOption.update_forward_refs()
FirstLevelCategory.update_forward_refs()
SecondLevelCategory.update_forward_refs()
PopularBlockCategories.update_forward_refs()
PopularBlock.update_forward_refs()
CatalogServiceBlock.update_forward_refs()
CatalogOtherServiceBlock.update_forward_refs()
NotificationType.update_forward_refs()
SimpleNotification.update_forward_refs()
PushEvent.update_forward_refs()
Offer.update_forward_refs()
OrderHeader.update_forward_refs()
OrderedExtra.update_forward_refs()
Interlocutor.update_forward_refs()
Package.update_forward_refs()
PackageItem.update_forward_refs()
Error.update_forward_refs()
Paging.update_forward_refs()
ProfileKwork.update_forward_refs()
Resize.update_forward_refs()
User.update_forward_refs()
FavouriteCategory.update_forward_refs()
UserReview.update_forward_refs()
Versions.update_forward_refs()
WantPayer.update_forward_refs()
WantsList.update_forward_refs()
ExchangeInfo.update_forward_refs()
Connects.update_forward_refs()
BudgetWithCount.update_forward_refs()
WantsFilter.update_forward_refs()
Attribute.update_forward_refs()
Attributes.update_forward_refs()
TrackFile.update_forward_refs()
Track.update_forward_refs()
ParentCategory.update_forward_refs()
DialogMessage.update_forward_refs()
FileWithSize.update_forward_refs()
FileWithMiniature.update_forward_refs()
GetMessage.update_forward_refs()
GetMessageWithTrack.update_forward_refs()
UserNotification.update_forward_refs()
OrderNotification.update_forward_refs()
StageNotification.update_forward_refs()
KworkNotification.update_forward_refs()
Notification.update_forward_refs()
KworkFile.update_forward_refs()
PackageWithUpgrade.update_forward_refs()
PagingWithPages.update_forward_refs()
FavoriteKworks.update_forward_refs()
DialogLastMessage.update_forward_refs()
