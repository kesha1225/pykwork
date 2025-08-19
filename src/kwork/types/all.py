from __future__ import annotations

import pydantic


class Achievements(pydantic.BaseModel):
    pass


class KworkBadges(pydantic.BaseModel):
    pass


class InboxOrder(pydantic.BaseModel):
    order_id: int | None = pydantic.Field(
        None,
        description="ID заказа",
    )
    status: str | None = pydantic.Field(
        None,
        description="Состояние предложения: new - Предложение в силе, cancel - Отказ, done - Заказ создан",
    )
    budget: int | None = pydantic.Field(
        None,
        description="Бюджет",
    )
    duration: int | None = pydantic.Field(
        None,
        description="срок выполнения (секунд); null - срок не ограничен",
    )
    kwork: dict | None = pydantic.Field(
        None,
        description="Объект кворка",
    )
    order: dict | None = pydantic.Field(
        None,
        description="Объект заказа",
    )


class TrackOrder(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="ID заказа",
    )
    title: str | None = pydantic.Field(
        None,
        description="Название заказа",
    )
    color: int | None = pydantic.Field(
        None,
        description="Цвет заказа",
    )
    worker_id: int | None = pydantic.Field(
        None,
        description="ID продавца",
    )


class Portfolio(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор",
    )
    title: str | None = pydantic.Field(
        None,
        description="Название работы",
    )
    order_id: int | None = pydantic.Field(
        None,
        description="ID заказа",
    )
    category_id: int | None = pydantic.Field(
        None,
        description="ID категории заказа",
    )
    category_name: str | None = pydantic.Field(
        None,
        description="Название категории заказа",
    )
    type: str | None = pydantic.Field(
        None,
        description="Тип, 'photo' или 'видео'",
    )
    photo: str | None = pydantic.Field(
        None,
        description="Относительный путь к фото",
    )
    video: str | None = pydantic.Field(
        None,
        description="Относительный путь к видео",
    )
    likes: int | None = pydantic.Field(
        None,
        description="Кол-во чистых лайков",
    )
    likes_dirty: int | None = pydantic.Field(
        None,
        description="Кол-во грязных лайков",
    )
    views: int | None = pydantic.Field(
        None,
        description="Кол-во чистых просмотров",
    )
    views_dirty: int | None = pydantic.Field(
        None,
        description="Кол-во грязных просмотров",
    )
    comments_count: int | None = pydantic.Field(
        None,
        description="Кол-во комментариев",
    )
    is_liked: bool | None = pydantic.Field(
        None,
        description="Стоит ли лайк пользователя",
    )
    images: list[dict] | None = pydantic.Field(
        None,
        description="Изображения, прикрепленные к портфолио",
    )
    videos: list[dict] | None = pydantic.Field(
        None,
        description="Видеоролики, прикрепленные к портфолио",
    )


class ProfilePortfolios(pydantic.BaseModel):
    pass


class UserAnswer(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор ответа",
    )
    text: str | None = pydantic.Field(
        None,
        description="Текст ответа",
    )
    user_id: int | None = pydantic.Field(
        None,
        description="Идентификатор пользователя - продавца",
    )
    time_added: int | None = pydantic.Field(
        None,
        description="Дата ответа UNIXTIME",
    )
    username: str | None = pydantic.Field(
        None,
        description="Имя пользователя",
    )
    profilepicture: str | None = pydantic.Field(
        None,
        description="""Ссылка на изображения аватара
	 *     пользователя""",
    )


class ProfileKworks(pydantic.BaseModel):
    pass


class UserWorker(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор продавца",
    )
    username: str | None = pydantic.Field(
        None,
        description="Имя пользователя",
    )
    fullname: str | None = pydantic.Field(
        None,
        description="Полное имя пользователя",
    )
    profilepicture: str | None = pydantic.Field(
        None,
        description="Путь к аватару",
    )
    rating: int | None = pydantic.Field(
        None,
        description="Рейтинг по пятибальной шкале",
    )
    reviews_count: int | None = pydantic.Field(
        None,
        description="Общее количество отзывов",
    )
    rating_count: int | None = pydantic.Field(
        None,
        description="Количество отзывов",
    )
    is_online: bool | None = pydantic.Field(
        None,
        description="Онлайн ли пользователь",
    )


class ProfileBadges(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор",
    )
    name: str | None = pydantic.Field(
        None,
        description="Название",
    )
    description: str | None = pydantic.Field(
        None,
        description="Описание",
    )
    image_url: str | None = pydantic.Field(
        None,
        description="Ссылка на изображение",
    )


class UserReviewWriter(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор продавца",
    )
    username: str | None = pydantic.Field(
        None,
        description="Имя пользователя",
    )
    profilepicture: str | None = pydantic.Field(
        None,
        description="Ссылка на изображения аватара пользователя",
    )


class WantWorker(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="ID запроса(проекта)",
    )
    user_id: int | None = pydantic.Field(
        None,
        description="ID пользователя",
    )
    username: str | None = pydantic.Field(
        None,
        description="Логин пользователя",
    )
    profile_picture: str | None = pydantic.Field(
        None,
        description="Изображение профиля",
    )
    price: int | None = pydantic.Field(
        None,
        description="Бюджет проекта",
    )
    title: str | None = pydantic.Field(
        None,
        description="Заголовок",
    )
    description: str | None = pydantic.Field(
        None,
        description="Краткое описание проекта",
    )
    offers: int | None = pydantic.Field(
        None,
        description="Количество предложений",
    )
    time_left: int | None = pydantic.Field(
        None,
        description="Время, оставшееся до закрытия проекта UNIX",
    )
    parent_category_id: int | None = pydantic.Field(
        None,
        description="Идентификатор рубрики проекта",
    )
    category_id: int | None = pydantic.Field(
        None,
        description="Идентификатор подрубрики проекта",
    )
    date_confirm: int | None = pydantic.Field(
        None,
        description="Дата первого подтверждения модератором (или переподтвержения при перезапуске из архива)",
    )
    category_base_price: int | None = pydantic.Field(
        None,
        description="Базовая стоимость работ в категории запроса",
    )
    user_projects_count: int | None = pydantic.Field(
        None,
        description="Количество проектов на бирже покупателя",
    )
    user_hired_percent: int | None = pydantic.Field(
        None,
        description="Процент нанятых продавцов на бирже",
    )
    achievements_list: list[Achievements] | None = pydantic.Field(
        None,
        description="",
    )
    is_viewed: bool | None = pydantic.Field(
        None,
        description="Просмотрен ли текущим пользователем",
    )
    already_work: int | None = pydantic.Field(
        None,
        description="Статус последнего заказа между пользователями",
    )
    allow_higher_price: bool | None = pydantic.Field(
        None,
        description="Готов ли покупатель рассмотреть предложения с ценой выше",
    )
    possible_price_limit: int | None = pydantic.Field(
        None,
        description="Лимит цены предложений с учетом готовности покупателя рассмотреть предложения с ценой выше",
    )


class TrackQuote(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор сообщения",
    )
    text: str | None = pydantic.Field(
        None,
        description="Текст сообщения",
    )
    from_id: int | None = pydantic.Field(
        None,
        description="Идентификатор отправителя",
    )
    files: list[TrackFile] | None = pydantic.Field(
        None,
        description="Данные об изображениях",
    )


class Achievement(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор",
    )
    name: str | None = pydantic.Field(
        None,
        description="Название",
    )
    description: str | None = pydantic.Field(
        None,
        description="Описание",
    )
    image_url: str | None = pydantic.Field(
        None,
        description="Ссылка на изображение",
    )


class VolumeType(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор",
    )
    name: str | None = pydantic.Field(
        None,
        description="Наименование в единственном числе",
    )
    name_short: str | None = pydantic.Field(
        None,
        description="Сокращенное наименование",
    )
    name_plural_2_4: str | None = pydantic.Field(
        None,
        description="Наименование во множественном числе, от 2 до 4",
    )
    name_plural_11_19: str | None = pydantic.Field(
        None,
        description="Наименование во множественном числе, от 11 до 19",
    )
    name_accusative: str | None = pydantic.Field(
        None,
        description="Наименование в винительном падеже",
    )
    volume_type_group_id: str | None = pydantic.Field(
        None,
        description="Идентификатор группы объема услуг",
    )
    contains_value: str | None = pydantic.Field(
        None,
        description="Количество в других единицах",
    )
    contains_id: str | None = pydantic.Field(
        None,
        description="Единица объема для contains_value",
    )
    group_order: str | None = pydantic.Field(
        None,
        description="Сортировка для группы",
    )
    lang: str | None = pydantic.Field(
        None,
        description="Язык",
    )


class PositiveReviewsCount(pydantic.BaseModel):
    pass


class Category(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор",
    )
    name: str | None = pydantic.Field(
        None,
        description="Название",
    )
    description: str | None = pydantic.Field(
        None,
        description="Описание",
    )


class ComplainCategory(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор",
    )
    title: str | None = pydantic.Field(
        None,
        description="Название",
    )
    commentRequired: bool | None = pydantic.Field(
        None,
        description="Обязателен ли комментарий для данной категории жалоб",
    )
    isFileUploaderNotAuth: bool | None = pydantic.Field(
        None,
        description="Разрешено ли загружать файлы",
    )
    hasNotification: bool | None = pydantic.Field(
        None,
        description="Название",
    )
    subCategories: list[ComplainCategory] | None = pydantic.Field(
        None,
        description="Подкатегории жалобы",
    )


class KworkLinkSiteItem(pydantic.BaseModel):
    name: str | None = pydantic.Field(
        None,
        description="Наименование площадки/сайта/домена",
    )
    sqi: str | None = pydantic.Field(
        None,
        description="ИКС",
    )
    moz_domain_authority: str | None = pydantic.Field(
        None,
        description="Moz Domain Authority",
    )
    moz_spam_score: str | None = pydantic.Field(
        None,
        description="Moz Spam Score",
    )
    majestic_citation_flow: str | None = pydantic.Field(
        None,
        description="Majestic",
    )
    trust: str | None = pydantic.Field(
        None,
        description="Траст",
    )
    spam: str | None = pydantic.Field(
        None,
        description="Спам",
    )
    language: str | None = pydantic.Field(
        None,
        description="Язык",
    )
    traffic: str | None = pydantic.Field(
        None,
        description="Трафик (поле присутствует у площадки и сайта)",
    )


class File(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор файла",
    )
    name: str | None = pydantic.Field(
        None,
        description="Имя файла",
    )
    path: str | None = pydantic.Field(
        None,
        description="Путь к файлу",
    )


class ShortUserInfo(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор юзера",
    )
    username: str | None = pydantic.Field(
        None,
        description="Имя юзера",
    )
    description: str | None = pydantic.Field(
        None,
        description="Описание",
    )
    profilepicture: str | None = pydantic.Field(
        None,
        description="Аватар",
    )
    rating: int | None = pydantic.Field(
        None,
        description="Рейтинг по пятибальной шкале",
    )
    rating_count: int | None = pydantic.Field(
        None,
        description="Кол-во оценок",
    )
    reviews_count: int | None = pydantic.Field(
        None,
        description="Кол-во ревью",
    )
    good_reviews: int | None = pydantic.Field(
        None,
        description="Кол-во положительных отзывов",
    )
    bad_reviews: int | None = pydantic.Field(
        None,
        description="Кол-во отрицательных отзывов",
    )
    is_online: bool | None = pydantic.Field(
        None,
        description="Онлайн ли юзер",
    )
    level: str | None = pydantic.Field(
        None,
        description="Уровень пользователя",
    )
    location: str | None = pydantic.Field(
        None,
        description="Местонахождение и местное время",
    )
    order_done_count: int | None = pydantic.Field(
        None,
        description="Кол-во выполненных заказов",
    )
    answer_time: str | None = pydantic.Field(
        None,
        description="Время ответа",
    )
    registration_time: int | None = pydantic.Field(
        None,
        description="Время регистрации UNIXTIME",
    )
    achievments_list: list[ProfileBadges] | None = pydantic.Field(
        None,
        description="Массив объектов наград",
    )


class KworkPackage(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор",
    )
    name: str | None = pydantic.Field(
        None,
        description="Название",
    )
    package_description: str | None = pydantic.Field(
        None,
        description="Описание",
    )
    price: int | None = pydantic.Field(
        None,
        description="Стоимость пакета",
    )
    term: str | None = pydantic.Field(
        None,
        description="Срок выполнения",
    )
    min: int | None = pydantic.Field(
        None,
        description="Минимальное значение",
    )
    max: int | None = pydantic.Field(
        None,
        description="Максимальное значение",
    )
    options: list[dict] | None = pydantic.Field(
        None,
        description="Опции пакета",
    )


class KworkInList(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор",
    )
    category_id: int | None = pydantic.Field(
        None,
        description="ID категории",
    )
    classifier_id: int | None = pydantic.Field(
        None,
        description="ID атрибута-значения классификации",
    )
    title: str | None = pydantic.Field(
        None,
        description="Название кворка",
    )
    image_url: str | None = pydantic.Field(
        None,
        description="Относительный путь к обложке кворка",
    )
    price: int | None = pydantic.Field(
        None,
        description="Стоимость кворка",
    )
    is_price_from: bool | None = pydantic.Field(
        None,
        description="Необходима ли подпись 'Цена ОТ'",
    )
    is_best: bool | None = pydantic.Field(
        None,
        description="Кворк имеет высший рейтинг",
    )
    is_hidden: bool | None = pydantic.Field(
        None,
        description="Кворк скрыт у активного юзера",
    )
    is_favorite: bool | None = pydantic.Field(
        None,
        description="Кворк в избранных у активного юзера",
    )
    is_viewed: bool | None = pydantic.Field(
        None,
        description="Просмотрен ли кворк",
    )
    isSubscription: bool | None = pydantic.Field(
        None,
        description="Кворк с подпиской?",
    )
    lang: str | None = pydantic.Field(
        None,
        description="Язык кворка, для привзяки валюты",
    )
    worker: UserWorker | None = pydantic.Field(
        None,
        description="",
    )
    badges: KworkBadges | None = pydantic.Field(
        None,
        description="",
    )


class CancelReason(pydantic.BaseModel):
    id: str | None = pydantic.Field(
        None,
        description="Идентификатор причины",
    )
    title: str | None = pydantic.Field(
        None,
        description="Наименование причины",
    )
    commentRequired: bool | None = pydantic.Field(
        None,
        description="Возможность добавлять комментарии",
    )
    subtypes: list[dict] | None = pydantic.Field(
        None,
        description="Достпуные дочерние причины отмены",
    )


class InboxMessage(pydantic.BaseModel):
    message_id: int | None = pydantic.Field(
        None,
        description="ID сообщений",
    )
    to_id: int | None = pydantic.Field(
        None,
        description="ID получаетеля",
    )
    to_username: str | None = pydantic.Field(
        None,
        description="Username получателя",
    )
    to_live_date: int | None = pydantic.Field(
        None,
        description="Дата последней активности получателя на сайте UNIXTIME",
    )
    from_id: int | None = pydantic.Field(
        None,
        description="Идентификатор пользователя отправителя",
    )
    from_username: str | None = pydantic.Field(
        None,
        description="Имя пользователя отправителя",
    )
    from_live_date: int | None = pydantic.Field(
        None,
        description="Дата последней активности отправителя на сайте UNIXTIME",
    )
    from_profilepicture: str | None = pydantic.Field(
        None,
        description="Ссылка на аватар отправителя",
    )
    to_profilepicture: str | None = pydantic.Field(
        None,
        description="Ссылка на аватар получателя",
    )
    message: str | None = pydantic.Field(
        None,
        description="Текст сообщения. Возможен HTML",
    )
    time: int | None = pydantic.Field(
        None,
        description="Дата сообщения UNIXTIME",
    )
    unread: bool | None = pydantic.Field(
        None,
        description="Сообщение непрочитано",
    )
    type: str | None = pydantic.Field(
        None,
        description="""Тип сообщения: NULL - обычное сообщение,
	 * 					custom_request - Запрос на индивидуальный кворк, offer_kwork_new - Предложение кворка,
	 *     				offer_kwork_payer_cancel - Предложение индивидуального кворка отклонено покупателем,
	 *     				offer_kwork_worker_cancel - Предложение индивидуального кворка отклонено продавцом,
	 *     				offer_kwork_done - Заказ создан, auto - Автоуведомление, support - Сообщение от техподдержки,
	 *     				report - Жалоба на пользователя""",
    )
    status: str | None = pydantic.Field(
        None,
        description="Заглушка после удаления поля 'status'",
    )
    created_order_id: int | None = pydantic.Field(
        None,
        description="Id созданного заказа индивидуального предложения",
    )
    forwarded: bool | None = pydantic.Field(
        None,
        description="Флаг является ли сообщение пересланным",
    )
    updated_at: int | None = pydantic.Field(
        None,
        description="Время изменения сообщения в Unixtime, или null",
    )
    warning_type: str | None = pydantic.Field(
        None,
        description="""флаги для получение статуса игнорирования сообщения
	 * 					(check — постановка сообщения на проверку, answer — на сообщение был ответ, ignore — сообщение было проигнорировано)""",
    )
    countup: int | None = pydantic.Field(
        None,
        description="Количество часов до ответа, -1 - значение не задано",
    )
    files: list[FileWithMiniature] | None = pydantic.Field(
        None,
        description="файлы сообщения",
    )
    quote: dict | None = pydantic.Field(
        None,
        description="Цитируемое сообщение",
    )
    message_page: int | None = pydantic.Field(
        None,
        description="Страница на которой находится сообщение",
    )
    custom_request: dict | None = pydantic.Field(
        None,
        description="Запрос на индивидуальный кворк",
    )
    inbox_order: InboxOrder | None = pydantic.Field(
        None,
        description="",
    )


class InboxTrackMessage(pydantic.BaseModel):
    conversation_id: int | None = pydantic.Field(
        None,
        description="ID сообщений в conversation",
    )
    message_id: int | None = pydantic.Field(
        None,
        description="ID сообщений в Inbox/Track",
    )
    entity_type: int | None = pydantic.Field(
        None,
        description="Тип сообщения (9 - Inbox, 10 - Track",
    )
    to_id: int | None = pydantic.Field(
        None,
        description="ID получаетеля",
    )
    to_username: str | None = pydantic.Field(
        None,
        description="Username получателя",
    )
    to_live_date: int | None = pydantic.Field(
        None,
        description="Дата последней активности получателя на сайте UNIXTIME",
    )
    from_id: int | None = pydantic.Field(
        None,
        description="Идентификатор пользователя отправителя",
    )
    from_username: str | None = pydantic.Field(
        None,
        description="Имя пользователя отправителя",
    )
    from_live_date: int | None = pydantic.Field(
        None,
        description="Дата последней активности отправителя на сайте UNIXTIME",
    )
    from_profilepicture: str | None = pydantic.Field(
        None,
        description="Ссылка на аватар отправителя",
    )
    to_profilepicture: str | None = pydantic.Field(
        None,
        description="Ссылка на аватар получателя",
    )
    forwarder_from_id: int | None = pydantic.Field(
        None,
        description="Идентификатор пользователя, от которого переслано сообщение",
    )
    forwarded_from_username: str | None = pydantic.Field(
        None,
        description="Имя пользователя, от которого переслано сообщение",
    )
    message: str | None = pydantic.Field(
        None,
        description="Текст сообщения. Возможен HTML",
    )
    time: int | None = pydantic.Field(
        None,
        description="Дата сообщения UNIXTIME",
    )
    unread: bool | None = pydantic.Field(
        None,
        description="Сообщение непрочитано",
    )
    type: str | None = pydantic.Field(
        None,
        description="Тип сообщения: NULL - обычное сообщение, custom_request - Запрос на индивидуальный кворк, offer_kwork_new - Предложение кворка, offer_kwork_payer_cancel - Предложение индивидуального кворка отклонено покупателем, offer_kwork_worker_cancel - Предложение индивидуального кворка отклонено продавцом, offer_kwork_done - Заказ создан, auto - Автоуведомление, support - Сообщение от техподдержки, report - Жалоба на пользователя",
    )
    status: str | None = pydantic.Field(
        None,
        description="Заглушка после удаления поля 'status'",
    )
    created_order_id: int | None = pydantic.Field(
        None,
        description="Id созданного заказа индивидуального предложения",
    )
    forwarded: bool | None = pydantic.Field(
        None,
        description="Флаг является ли сообщение пересланным",
    )
    updated_at: int | None = pydantic.Field(
        None,
        description="Время изменения сообщения в Unixtime, или null",
    )
    warning_type: str | None = pydantic.Field(
        None,
        description="флаги для получение статуса игнорирования сообщения (check — постановка сообщения на проверку, answer — на сообщение был ответ, ignore — сообщение было проигнорировано)",
    )
    countup: int | None = pydantic.Field(
        None,
        description="Количество часов до ответа, -1 - значение не задано",
    )
    files: list[FileWithMiniature] | None = pydantic.Field(
        None,
        description="файлы сообщения",
    )
    quote: dict | None = pydantic.Field(
        None,
        description="Цитируемое сообщение",
    )
    message_page: int | None = pydantic.Field(
        None,
        description="Страница на которой находится сообщение",
    )
    custom_request: dict | None = pydantic.Field(
        None,
        description="Запрос на индивидуальный кворк",
    )
    inbox_order: InboxOrder | None = pydantic.Field(
        None,
        description="",
    )
    track_order: TrackOrder | None = pydantic.Field(
        None,
        description="",
    )


class OrderDetails(pydantic.BaseModel):
    details: dict | None = pydantic.Field(
        None,
        description="Детали заказа",
    )
    stages: list[dict] | None = pydantic.Field(
        None,
        description="Этапы заказа",
    )
    key_tracks: list[dict] | None = pydantic.Field(
        None,
        description="Треки заказа",
    )


class OrderOption(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор опции",
    )
    name: str | None = pydantic.Field(
        None,
        description="Наименование опции",
    )
    price: int | None = pydantic.Field(
        None,
        description="Стоимость опции",
    )
    currency: str | None = pydantic.Field(
        None,
        description="Валюта опции",
    )
    time: int | None = pydantic.Field(
        None,
        description="Добавочная длительность к заказу",
    )


class FirstLevelCategory(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор рубрики",
    )
    name: str | None = pydantic.Field(
        None,
        description="Название рубрики",
    )
    rubric_description: str | None = pydantic.Field(
        None,
        description="Описание",
    )
    ico: str | None = pydantic.Field(
        None,
        description="Иконка",
    )
    ico_extra: str | None = pydantic.Field(
        None,
        description="Иконка png",
    )
    order: int | None = pydantic.Field(
        None,
        description="Порядок сортировки",
    )
    category_image: str | None = pydantic.Field(
        None,
        description="Путь к изображению",
    )


class SecondLevelCategory(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор рубрики",
    )
    name: str | None = pydantic.Field(
        None,
        description="Название рубрики",
    )
    rubric_description: str | None = pydantic.Field(
        None,
        description="Описание",
    )
    order: int | None = pydantic.Field(
        None,
        description="Порядок сортировки",
    )
    category_image: str | None = pydantic.Field(
        None,
        description="Путь к изображению",
    )
    kworks_count: int | None = pydantic.Field(
        None,
        description="Количество кворков",
    )


class PopularBlockCategories(pydantic.BaseModel):
    category_id: int | None = pydantic.Field(
        None,
        description="Идентификатор категории, может быть null если это классификация",
    )
    classifier_id: int | None = pydantic.Field(
        None,
        description="Идентификатор классификации, может быть null если это категория",
    )
    name: str | None = pydantic.Field(
        None,
        description="Название рубрики",
    )
    order: int | None = pydantic.Field(
        None,
        description="Порядок сортировки",
    )
    cover_url: str | None = pydantic.Field(
        None,
        description="Путь к изображению",
    )
    kworks_count: int | None = pydantic.Field(
        None,
        description="Количество кворков",
    )


class PopularBlock(pydantic.BaseModel):
    name: str | None = pydantic.Field(
        None,
        description="Наименование блока",
    )
    block_description: str | None = pydantic.Field(
        None,
        description="Описание блока",
    )
    categories: list[PopularBlockCategories] | None = pydantic.Field(
        None,
        description="Массив категорий",
    )
    id: int | None = pydantic.Field(
        None,
        description="ID категории",
    )
    order: int | None = pydantic.Field(
        None,
        description="Порядок",
    )


class CatalogServiceBlock(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор категории",
    )
    name: str | None = pydantic.Field(
        None,
        description="Наименование",
    )
    rubric_description: str | None = pydantic.Field(
        None,
        description="Описание рубрики(основные категории)",
    )
    icon_path: str | None = pydantic.Field(
        None,
        description="Иконка рубрики",
    )
    order: int | None = pydantic.Field(
        None,
        description="Порядок сортировки",
    )


class CatalogOtherServiceBlock(pydantic.BaseModel):
    category_id: int | None = pydantic.Field(
        None,
        description="Идентификатор категории, может быть null если это классификация",
    )
    classifier_id: int | None = pydantic.Field(
        None,
        description="Идентификатор классификации, может быть null если это категория",
    )
    name: str | None = pydantic.Field(
        None,
        description="Название рубрики",
    )
    order: int | None = pydantic.Field(
        None,
        description="Порядок сортировки",
    )
    cover_url: str | None = pydantic.Field(
        None,
        description="Путь к изображению",
    )


class NotificationType(pydantic.BaseModel):
    name: str | None = pydantic.Field(
        None,
        description="Название",
    )
    description: str | None = pydantic.Field(
        None,
        description="Описание",
    )
    is_red: bool | None = pydantic.Field(
        None,
        description="Важное ли",
    )
    priority: int | None = pydantic.Field(
        None,
        description="Приоритет",
    )
    entity_type: str | None = pydantic.Field(
        None,
        description="Тип связанной сущности",
    )
    notifications: list[Notification] | None = pydantic.Field(
        None,
        description="Уведомления данного типа",
    )


class SimpleNotification(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор",
    )
    added: int | None = pydantic.Field(
        None,
        description="Дата создания unixtime",
    )
    entity_id: int | None = pydantic.Field(
        None,
        description="Идентификатор связанной сущности",
    )
    link: str | None = pydantic.Field(
        None,
        description="Ссылка для перехода",
    )


class PushEvent(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор сквозной очереди непрочитанных push-событий",
    )
    entity_id: int | None = pydantic.Field(
        None,
        description="Идентификатор сущности, связанной с push-событием (inbox_id, notity_id",
    )
    user_id: int | None = pydantic.Field(
        None,
        description="Идентификатор пользователя-получателя (текущий)",
    )
    data: dict | None = pydantic.Field(
        None,
        description="Данные push-события (свой набор для каждой сущности)",
    )
    created_at: str | None = pydantic.Field(
        None,
        description="Дата создания события",
    )
    event: str | None = pydantic.Field(
        None,
        description="Наименование события",
    )


class Offer(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор предложения",
    )
    status: str | None = pydantic.Field(
        None,
        description="Статус предложения",
    )
    title: str | None = pydantic.Field(
        None,
        description="Название предложения",
    )
    comment: str | None = pydantic.Field(
        None,
        description="Комментарий к предложению",
    )
    price: int | None = pydantic.Field(
        None,
        description="Цена предложения",
    )
    duration: int | None = pydantic.Field(
        None,
        description="Срок выполнения дней",
    )
    date_create: int | None = pydantic.Field(
        None,
        description="Дата создания предложения",
    )
    is_actual: bool | None = pydantic.Field(
        None,
        description="Флаг актуальности предложения",
    )
    is_read: bool | None = pydantic.Field(
        None,
        description="Флаг прочитанности предложения покупателем",
    )
    want_id: int | None = pydantic.Field(
        None,
        description="Идентификатор запроса на услугу",
    )
    order_id: int | None = pydantic.Field(
        None,
        description="Идентификатор заказа",
    )
    kwork_id: int | None = pydantic.Field(
        None,
        description="Идентификатор кворка",
    )
    project: WantWorker | None = pydantic.Field(
        None,
        description="",
    )


class OrderHeader(pydantic.BaseModel):
    order: dict | None = pydantic.Field(
        None,
        description="Данные заказа",
    )
    kwork: dict | None = pydantic.Field(
        None,
        description="Данные кворка",
    )
    worker: dict | None = pydantic.Field(
        None,
        description="Данные продавца",
    )
    payer: dict | None = pydantic.Field(
        None,
        description="Данные покупателя",
    )


class OrderedExtra(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="ID опции",
    )
    title: str | None = pydantic.Field(
        None,
        description="Название опции",
    )
    count: int | None = pydantic.Field(
        None,
        description="Количество заказанных опций",
    )
    payer_price: int | None = pydantic.Field(
        None,
        description="Цена заказанных опции для покупателя",
    )
    worker_price: int | None = pydantic.Field(
        None,
        description="Цена заказанных опции для продавца",
    )
    totaldays: int | None = pydantic.Field(
        None,
        description="Общая длительность в днях",
    )


class Interlocutor(pydantic.BaseModel):
    user_id: int | None = pydantic.Field(
        None,
        description="Идентификатор пользователя",
    )
    username: str | None = pydantic.Field(
        None,
        description="Имя пользователя",
    )
    last_online_timestamp: int | None = pydantic.Field(
        None,
        description="Последнее время в сети (unixtime)",
    )
    avatar_image_path: str | None = pydantic.Field(
        None,
        description="Абсолютный урл аватара",
    )


class Package(pydantic.BaseModel):
    description: str | None = pydantic.Field(
        None,
        description="Описание пакета",
    )
    price: int | None = pydantic.Field(
        None,
        description="Цена пакета",
    )
    duration: int | None = pydantic.Field(
        None,
        description="Продолжительность в днях",
    )
    type: str | None = pydantic.Field(
        None,
        description="Тип пакета",
    )
    items: list[PackageItem] | None = pydantic.Field(
        None,
        description="Массив опций пакета",
    )


class PackageItem(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор опции пакета",
    )
    name: str | None = pydantic.Field(
        None,
        description="Название опции",
    )
    value: str | None = pydantic.Field(
        None,
        description="Значение опции",
    )
    type: str | None = pydantic.Field(
        None,
        description="Тип значения опции",
    )
    name_1: str | None = pydantic.Field(
        None,
        description="Название опции в единственном числе",
    )
    name_2: str | None = pydantic.Field(
        None,
        description="Название опции для 2",
    )
    name_5: str | None = pydantic.Field(
        None,
        description="Название опции для 5",
    )


class Error(pydantic.BaseModel):
    success: bool | None = pydantic.Field(
        None,
        description="Флаг успешности",
    )
    error: str | None = pydantic.Field(
        None,
        description="Текст ошибки",
    )
    error_code: int | None = pydantic.Field(
        None,
        description="Код ошибки",
    )


class Paging(pydantic.BaseModel):
    page: int | None = pydantic.Field(
        None,
        description="Текущая страница",
    )
    total: int | None = pydantic.Field(
        None,
        description="Общее количество элементов",
    )
    limit: int | None = pydantic.Field(
        None,
        description="Количество элементов на странице",
    )


class ProfileKwork(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор",
    )
    category_id: int | None = pydantic.Field(
        None,
        description="ID категории",
    )
    category_name: str | None = pydantic.Field(
        None,
        description="Название категории",
    )
    classification_id: int | None = pydantic.Field(
        None,
        description="ID атрибута-значения классификации верхнего уровня",
    )
    status_id: int | None = pydantic.Field(
        None,
        description="Идентификатор статуса кворка",
    )
    status_name: str | None = pydantic.Field(
        None,
        description="Название статуса",
    )
    title: str | None = pydantic.Field(
        None,
        description="Название кворка",
    )
    image_url: str | None = pydantic.Field(
        None,
        description="Относительный путь к обложке кворка",
    )
    price: int | None = pydantic.Field(
        None,
        description="Стоимость кворка",
    )
    is_price_from: bool | None = pydantic.Field(
        None,
        description="Необходима ли подпись 'Цена ОТ'",
    )
    is_best: bool | None = pydantic.Field(
        None,
        description="Кворк имеет высший рейтинг",
    )
    is_hidden: bool | None = pydantic.Field(
        None,
        description="Кворк скрыт у активного юзера",
    )
    is_favorite: bool | None = pydantic.Field(
        None,
        description="Кворк в избранных у активного юзера",
    )
    is_viewed: bool | None = pydantic.Field(
        None,
        description="Просмотрен ли кворк",
    )
    isSubscription: bool | None = pydantic.Field(
        None,
        description="Кворк с подпиской?",
    )
    lang: str | None = pydantic.Field(
        None,
        description="Язык кворка, для привзяки валюты",
    )
    order: int | None = pydantic.Field(
        None,
        description="Порядок вывода в списке",
    )
    worker: UserWorker | None = pydantic.Field(
        None,
        description="",
    )
    edits_list: list[str] | None = pydantic.Field(
        None,
        description="Массив строк что нужно исправить в кворке, для текущего юзера",
    )
    activity: dict | None = pydantic.Field(
        None,
        description="Активность для текущего юзера",
    )
    badges: KworkBadges | None = pydantic.Field(
        None,
        description="",
    )


class Resize(pydantic.BaseModel):
    x: int | None = pydantic.Field(
        None,
        description="Сдвиг по вертикали в % от ширины оригинального изображения",
    )
    y: int | None = pydantic.Field(
        None,
        description="Сдвиг по горизонтали в % от высоты оригинального изображения",
    )
    w: int | None = pydantic.Field(
        None,
        description="Ширина в % от ширины оригинального изображения",
    )
    h: int | None = pydantic.Field(
        None,
        description="Высота в % от ширины оригинального изображения",
    )


class User(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор пользователя",
    )
    username: str | None = pydantic.Field(
        None,
        description="Имя пользователя",
    )
    profilepicture: str | None = pydantic.Field(
        None,
        description="Путь к изображению аватара",
    )
    description: str | None = pydantic.Field(
        None,
        description="Текст о себе",
    )
    slogan: str | None = pydantic.Field(
        None,
        description="Слоган - не заполнен",
    )
    fullname: str | None = pydantic.Field(
        None,
        description="Настоящее имя",
    )
    level_description: str | None = pydantic.Field(
        None,
        description="Название уровня продавца",
    )
    cover: str | None = pydantic.Field(
        None,
        description="Путь к баннеру пользователя",
    )
    good_reviews: int | None = pydantic.Field(
        None,
        description="Количество положительных отзывов",
    )
    bad_reviews: int | None = pydantic.Field(
        None,
        description="Количество отрицательных отзывов",
    )
    reviews_count: int | None = pydantic.Field(
        None,
        description="Общее количество отзывов",
    )
    location: str | None = pydantic.Field(
        None,
        description="Город или страна",
    )
    rating: str | None = pydantic.Field(
        None,
        description="Рейтинг по 5 бальной шкале с 1 десятичным знаком",
    )
    rating_count: int | None = pydantic.Field(
        None,
        description="Количество отзывов",
    )
    online: bool | None = pydantic.Field(
        None,
        description="Онлайн ли пользователь",
    )
    live_date: int | None = pydantic.Field(
        None,
        description="Дата последней активности на сайте",
    )
    custom_request_min_budget: int | None = pydantic.Field(
        None,
        description="Минимальный бюджет запроса на индивидуальный кворк (представлен только в случае если пользователь авторизован)",
    )
    is_allow_custom_request: bool | None = pydantic.Field(
        None,
        description="Принимает ли пользователь запросы на индивидуальные кворки",
    )
    order_done_persent: int | None = pydantic.Field(
        None,
        description="Процент успешно сданных заказов",
    )
    order_done_intime_persent: int | None = pydantic.Field(
        None,
        description="Процент сданных вовремя заказов",
    )
    order_done_repeat_persent: int | None = pydantic.Field(
        None,
        description="Процент повторных заказов",
    )
    timezoneId: int | None = pydantic.Field(
        None,
        description="id временной зоны",
    )
    blocked_by_user: bool | None = pydantic.Field(
        None,
        description="Заблокирован ли диалог с пользователем (всегда false если запрос от неавторизованного пользователя)",
    )
    allowedDialog: bool | None = pydantic.Field(
        None,
        description="Разрешено ли писать пользователю",
    )
    addtime: int | None = pydantic.Field(
        None,
        description="Дата регистрации",
    )
    achievments_list: list[ProfileBadges | None] = pydantic.Field(
        None,
        description="",
    )
    completed_orders_count: int | None = pydantic.Field(
        None,
        description="Количество выполненных заказов",
    )
    profession: str | None = pydantic.Field(
        None,
        description="Специальность пользователя",
    )
    kworks_count: int | None = pydantic.Field(
        None,
        description="Количество активных кворков",
    )
    kworks: ProfileKworks | None = pydantic.Field(
        None,
        description="",
    )
    portfolio_list: ProfilePortfolios | None = pydantic.Field(
        None,
        description="",
    )
    reviews: list[UserReview] | None = pydantic.Field(
        None,
        description="Массив отзывов",
    )


class FavouriteCategory(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="ID категории",
    )
    name: str | None = pydantic.Field(
        None,
        description="Название категории",
    )


class UserReview(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор отзыва. Может быть NULL если это портфолио",
    )
    time_added: int | None = pydantic.Field(
        None,
        description="Дата добавления отзыва или портфолио UNIXTIME",
    )
    text: str | None = pydantic.Field(
        None,
        description="Текст отзыва. Может быть NULL если это портфолио",
    )
    auto_mode: str | None = pydantic.Field(
        None,
        description="Статус автоматического создания отзыва: inwork_time_over - Просрочено время взятия в работу, time_over - Просрочено время выполнения, incorrect_execute - Некорректное выполнение",
    )
    good: bool | None = pydantic.Field(
        None,
        description="Является ли отзыв положительным",
    )
    bad: bool | None = pydantic.Field(
        None,
        description="Является ли отзыв отрицательным",
    )
    kwork: dict | None = pydantic.Field(
        None,
        description="Объект кворка",
    )
    writer: UserReviewWriter | None = pydantic.Field(
        None,
        description="",
    )
    answer: UserAnswer | None = pydantic.Field(
        None,
        description="",
    )
    portfolio: Portfolio | None = pydantic.Field(
        None,
        description="",
    )


class Versions(pydantic.BaseModel):
    current_version_ios: str | None = pydantic.Field(
        None,
        description="Текущая версия iOS",
    )
    current_version_android: str | None = pydantic.Field(
        None,
        description="Текущая версия Android",
    )
    critical_update: bool | None = pydantic.Field(
        None,
        description="Обязательное обновление или рекомендуемое",
    )
    facebook: bool | None = pydantic.Field(
        None,
        description="Можно ли отображать facebook",
    )


class WantPayer(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор проекта",
    )
    title: str | None = pydantic.Field(
        None,
        description="Заголовок проекта",
    )
    description: str | None = pydantic.Field(
        None,
        description="Описание проекта",
    )
    status: str | None = pydantic.Field(
        None,
        description="Статус проекта",
    )
    want_status_id: int | None = pydantic.Field(
        None,
        description="Идентификатор статуса (альтернативный статус)",
    )
    date_create: int | None = pydantic.Field(
        None,
        description="Дата создания проекта",
    )
    date_active: int | None = pydantic.Field(
        None,
        description="Дата активации проекта",
    )
    date_expire: int | None = pydantic.Field(
        None,
        description="Дата окончания проекта",
    )
    date_reject: int | None = pydantic.Field(
        None,
        description="Дата отклонения проекта",
    )
    price_limit: int | None = pydantic.Field(
        None,
        description="Бюджет проекта",
    )
    views: int | None = pydantic.Field(
        None,
        description="Количество просмотров",
    )
    orders: int | None = pydantic.Field(
        None,
        description="Количество заказов по проекту",
    )
    offers: int | None = pydantic.Field(
        None,
        description="Количество предложений по проекту",
    )
    views_history: dict | None = pydantic.Field(
        None,
        description="Массив количества просмотров, сгруппированный по дням",
    )
    category_base_price: int | None = pydantic.Field(
        None,
        description="Базовая стоимость работ в категории запроса",
    )
    allow_higher_price: bool | None = pydantic.Field(
        None,
        description="Готов ли покупатель рассмотреть предложения с ценой выше",
    )
    possible_price_limit: int | None = pydantic.Field(
        None,
        description="Лимит цены предложений с учетом готовности покупателя рассмотреть предложения с ценой выше",
    )


class WantsList(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор статуса",
    )
    title: str | None = pydantic.Field(
        None,
        description="Отображаемое название статуса",
    )
    tootlip: str | None = pydantic.Field(
        None,
        description="Описание статуса",
    )
    order: int | None = pydantic.Field(
        None,
        description="Порядковый номер вкладки",
    )
    projects_count: int | None = pydantic.Field(
        None,
        description="Количество запросов на услугу в статусе",
    )
    wants: list[WantPayer] | None = pydantic.Field(
        None,
        description="Список заявок на услугу",
    )


class ExchangeInfo(pydantic.BaseModel):
    exchange_response_count: int | None = pydantic.Field(
        None,
        description="Количество моих откликов на бирже",
    )
    archived_count: int | None = pydantic.Field(
        None,
        description="Количество заархивированных проектов",
    )


class Connects(pydantic.BaseModel):
    all_connects: int | None = pydantic.Field(
        None,
        description="Кол-во коннектов продавца",
    )
    active_connects: int | None = pydantic.Field(
        None,
        description="Количество доступных коннектов",
    )
    update_time: int | None = pydantic.Field(
        None,
        description="Дата начисления коннектов (UNIX), -1 - дата начисления не определена (выводится как Н/Д)",
    )


class BudgetWithCount(pydantic.BaseModel):
    name: str | None = pydantic.Field(
        None,
        description="Наименование диапазона",
    )
    boundaries: dict | None = pydantic.Field(
        None,
        description="Диапазон цен",
    )
    count: int | None = pydantic.Field(
        None,
        description="Количество проектов в диапазоне",
    )


class WantsFilter(pydantic.BaseModel):
    categories: list[FavouriteCategory] | None = pydantic.Field(
        None,
        description="Массив объектов рубрик",
    )
    price_from: int | None = pydantic.Field(
        None,
        description="Бюджет от (не обязательно)",
    )
    price_to: int | None = pydantic.Field(
        None,
        description="Бюджет до (не обязательно)",
    )
    hiring_to: int | None = pydantic.Field(
        None,
        description="Процент найма от (не обязательно)",
    )
    kworks_filter_from: int | None = pydantic.Field(
        None,
        description="Количество предложений от (не обязательно)",
    )
    kworks_filter_to: int | None = pydantic.Field(
        None,
        description="Количество предложений до (не обязательно)",
    )


class Attribute(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор",
    )
    title: str | None = pydantic.Field(
        None,
        description="Название",
    )
    lang: str | None = pydantic.Field(
        None,
        description="Язык",
    )
    h1: str | None = pydantic.Field(
        None,
        description="Seo заголовок страницы",
    )
    hint_payer: str | None = pydantic.Field(
        None,
        description="Подсказка для покупателя",
    )
    hint_worker: str | None = pydantic.Field(
        None,
        description="Подсказка для продавца",
    )
    note_worker: str | None = pydantic.Field(
        None,
        description="Комментарий для продавца",
    )
    category_id: int | None = pydantic.Field(
        None,
        description="Идентификатор категории",
    )
    visible: int | None = pydantic.Field(
        None,
        description="Видимость",
    )
    is_classification: bool | None = pydantic.Field(
        None,
        description="Является классификацией",
    )
    required: bool | None = pydantic.Field(
        None,
        description="Обязателен выбор потомков при редактировании",
    )
    allow_multiple: bool | None = pydantic.Field(
        None,
        description="Разрешен множественный выбор потомков",
    )
    multiple_max_count: int | None = pydantic.Field(
        None,
        description="Максимальное количество выбранных потомков",
    )
    allow_custom: bool | None = pydantic.Field(
        None,
        description="Разрешено добавление пользовательских потомков",
    )
    portfolio: bool | None = pydantic.Field(
        None,
        description="Отображать портфолио на странице мои портфолио",
    )
    parent_portfolio: bool | None = pydantic.Field(
        None,
        description="Отображать портфолио на странице мои портфолио (унаследовано)",
    )
    is_custom: bool | None = pydantic.Field(
        None,
        description="Пользовательский",
    )
    custom_max_count: bool | None = pydantic.Field(
        None,
        description="Максимальное количество пользовательских потомков",
    )
    demo_file_upload: bool | None = pydantic.Field(
        None,
        description="Разрешена загрузка демо-отчета",
    )
    custom_moderation_status: str | None = pydantic.Field(
        None,
        description="Статус модерации пользовательского",
    )
    order_index: int | None = pydantic.Field(
        None,
        description="Приоритет сортировки",
    )
    is_free_price: bool | None = pydantic.Field(
        None,
        description="Свободная цена",
    )
    unembedded: bool | None = pydantic.Field(
        None,
        description="Отображать невложенным в основное дерево",
    )
    percent_usage: str | None = pydantic.Field(
        None,
        description="Процент использования в кворках",
    )
    portfolio_type: str | None = pydantic.Field(
        None,
        description="Разрешено портфолио",
    )
    orders_inprogress_limit: int | None = pydantic.Field(
        None,
        description="Количество заказов кворка, при котором он становится на паузу",
    )
    orders_inprogress_pause_off: int | None = pydantic.Field(
        None,
        description="Количество заказов кворка, при котором он снимается с паузы",
    )
    depth: int | None = pydantic.Field(
        None,
        description="Глубина в дереве",
    )
    is_custom_extra_denied: bool | None = pydantic.Field(
        None,
        description="Запрещено добавлять пакетные доп.опции в кворке",
    )
    is_subscribe_price: bool | None = pydantic.Field(
        None,
        description="Цена по подписке",
    )
    is_kwork_links_sites: int | None = pydantic.Field(
        None,
        description="Необходимость предоставления списка ссылок - 1, доменов - 2, сайтов - 3",
    )
    meta_title: str | None = pydantic.Field(
        None,
        description="Значение для meta тега title",
    )
    meta_description: str | None = pydantic.Field(
        None,
        description="Значение для meta тега description",
    )
    parent_id: int | None = pydantic.Field(
        None,
        description="Идентификатор родителя",
    )
    volume_type_id: int | None = pydantic.Field(
        None,
        description="Идентификатор числового объема",
    )
    base_volume: int | None = pydantic.Field(
        None,
        description="Базовый числовой объем",
    )
    min_volume: int | None = pydantic.Field(
        None,
        description="Минимальный числовой объем",
    )
    max_volume: int | None = pydantic.Field(
        None,
        description="Максимальный числовой объем",
    )
    min_volume_type_id: int | None = pydantic.Field(
        None,
        description="Идентификатор типа минимального числовой объема",
    )
    max_volume_type_id: int | None = pydantic.Field(
        None,
        description="Идентификатор типа максимального числовой объема",
    )
    custom_descendant_count: int | None = pydantic.Field(
        None,
        description="Количество пользовательских атрибутов среди потомков",
    )
    kworks_count: int | None = pydantic.Field(
        None,
        description="Количество активных кворков в которых используется атрибут",
    )
    alias: str | None = pydantic.Field(
        None,
        description="Алиас в каталоге",
    )
    duplicated_attribute_id: int | None = pydantic.Field(
        None,
        description="Идентификатор дублируемого атрибута",
    )
    twin_id: int | None = pydantic.Field(
        None,
        description="Идентификатор атрибута близнеца в другом языке",
    )
    is_smm_hide: bool | None = pydantic.Field(
        None,
        description="Является ли скрываемым по логике SMM",
    )
    children: list[Attribute] | None = pydantic.Field(
        None,
        description="Потомки",
    )


class Attributes(pydantic.BaseModel):
    pass


class TrackFile(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор файла",
    )
    name: int | None = pydantic.Field(
        None,
        description="Имя файла",
    )
    file_url: str | None = pydantic.Field(
        None,
        description="Абсолютный урл файла на сервере",
    )
    miniature_url: str | None = pydantic.Field(
        None,
        description="Абсолютный урл миниатюры",
    )
    size_in_bytes: int | None = pydantic.Field(
        None,
        description="Размер файла в байтах",
    )


class Track(pydantic.BaseModel):
    id: int | None = pydantic.Field(
        None,
        description="Идентификатор сообщения",
    )
    sent_timestamp: int | None = pydantic.Field(
        None,
        description="Время отправки UnixTime",
    )
    text: str | None = pydantic.Field(
        None,
        description="Текст сообщения",
    )
    from_id: int | None = pydantic.Field(
        None,
        description="Идентификатор отправителя",
    )
    from_name: str | None = pydantic.Field(
        None,
        description="Имя отправителя",
    )
    files: list[TrackFile] | None = pydantic.Field(
        None,
        description="Данные об изображениях",
    )
    is_unread: bool | None = pydantic.Field(
        None,
        description="Прочитано ли сообщение",
    )
    updated_at: int | None = pydantic.Field(
        None,
        description="Время изменения сообщения, UnixTime",
    )
    quote: TrackQuote | None = pydantic.Field(
        None,
        description="",
    )
    type: int | None = pydantic.Field(
        None,
        description="Тип сообщения",
    )


class ParentCategory(Category):
    subcategories: list[Category] | None = pydantic.Field(
        None,
        description="Подкатегории",
    )


class DialogMessage(pydantic.BaseModel):
    unread_count: int | None = pydantic.Field(
        None,
        description="Количество непрочитанных сообщений",
    )
    last_message: str | None = pydantic.Field(
        None,
        description="Текст последнего сообщения",
    )
    time: int | None = pydantic.Field(
        None,
        description="Время последнего сообщения UNIXTIME",
    )
    user_id: int | None = pydantic.Field(
        None,
        description="Идентификатор пользователя-собеседника",
    )
    username: str | None = pydantic.Field(
        None,
        description="Имя пользователя - собеседника",
    )
    profilepicture: str | None = pydantic.Field(
        None,
        description="Ссылка на аватар пользователя - собеседника",
    )
    is_online: bool | None = pydantic.Field(
        None,
        description="Онлайн ли собеседник",
    )
    lastOnlineTime: int | None = pydantic.Field(
        None,
        description="Время, когда пользователь был последний раз онлайн",
    )
    link: str | None = pydantic.Field(
        None,
        description="Ссылка страницы, на которую должен попадать пользователь",
    )
    status: str | None = pydantic.Field(
        None,
        description="Заглушка после удаления поля 'status'",
    )
    blocked_by_user: bool | None = pydantic.Field(
        None,
        description="Заблокирован ли диалог с пользователем - собеседником",
    )
    allowedDialog: bool | None = pydantic.Field(
        None,
        description="Разрешено ли писать пользователю - собеседнику",
    )
    lastMessage: DialogLastMessage | None = pydantic.Field(
        None,
        description="",
    )
    has_active_order: bool | None = pydantic.Field(
        None,
        description="Есть ли активный заказ среди собеседников",
    )
    archived: bool | None = pydantic.Field(
        None,
        description="Является ли диалог архивным или нет",
    )
    isStarred: bool | None = pydantic.Field(
        None,
        description="Помечен ли диалог как избранный",
    )
    warning_message_id: int | None = pydantic.Field(
        None,
        description="id сообщения на которое требуется обязательный ответ",
    )
    countup: int | None = pydantic.Field(
        None,
        description="Количество часов до ответа, -1 - значение не задано",
    )
    has_answer: bool | None = pydantic.Field(
        None,
        description="Был ли ответ в диалоге пользователей",
    )
    is_allow_custom_request: bool | None = pydantic.Field(
        None,
        description="Принимает ли пользователь запросы на индивидуальный кворк",
    )
    hidden_at: int | None = pydantic.Field(
        None,
        description="Время скрытия/удаления диалога",
    )
    disallowReason: int | None = pydantic.Field(
        None,
        description="Причина невозможности ведения диалога",
    )


class FileWithSize(File):
    size: int | None = pydantic.Field(
        None,
        description="Размер в байтах",
    )
    timestamp: int | None = pydantic.Field(
        None,
        description="Дата создания",
    )
    status: str | None = pydantic.Field(
        None,
        description="Статус",
    )


class FileWithMiniature(FileWithSize):
    miniature_url: str | None = pydantic.Field(
        None,
        description="Ссылка на файл с миниатюрой",
    )
    miniature_path: str | None = pydantic.Field(
        None,
        description="Путь к файлу миниатюры",
    )
    imageData: dict | None = pydantic.Field(
        None,
        description="Данные низкокачественного изображения",
    )


class GetMessage(InboxMessage):
    page: int | None = pydantic.Field(
        None,
        description="Номер страницы где находится сообщение",
    )


class GetMessageWithTrack(InboxTrackMessage):
    page: int | None = pydantic.Field(
        None,
        description="Номер страницы где находится сообщение",
    )


class UserNotification(SimpleNotification):
    otherUserId: int | None = pydantic.Field(
        None,
        description="Идентификатор другого пользователя",
    )
    otherUserName: str | None = pydantic.Field(
        None,
        description="Имя другого пользователя",
    )
    otherUserAvatar: str | None = pydantic.Field(
        None,
        description="Ссылка на изображение аватара другого пользователя",
    )
    isOtherUserOnline: bool | None = pydantic.Field(
        None,
        description="Онлайн ли другой пользователь",
    )


class OrderNotification(UserNotification):
    orderId: int | None = pydantic.Field(
        None,
        description="Идентификатор заказа",
    )
    orderTitle: str | None = pydantic.Field(
        None,
        description="Название заказа",
    )


class StageNotification(OrderNotification):
    stageTitle: str | None = pydantic.Field(
        None,
        description="Название этапа",
    )


class KworkNotification(SimpleNotification):
    kworkTitle: str | None = pydantic.Field(
        None,
        description="Название кворка",
    )


class Notification(
    KworkNotification,
    StageNotification,
):
    pass


class KworkFile(FileWithSize):
    type: str | None = pydantic.Field(
        None,
        description="Тип файла: kwork_description - Файл для описания кворка, kwork_instruction - Файл для инструкции",
    )


class PackageWithUpgrade(Package):
    upgrade: Package | None = pydantic.Field(
        None,
        description="",
    )


class PagingWithPages(Paging):
    pages: int | None = pydantic.Field(
        None,
        description="Количество страниц",
    )


class FavoriteKworks(ProfileKwork):
    classifier_id: int | None = pydantic.Field(
        None,
        description="ID последнего атрибута/классификации",
    )


class DialogLastMessage(pydantic.BaseModel):
    unread: bool | None = pydantic.Field(
        None,
        description="Было ли прочитано последнне сообщение",
    )
    fromUsername: str | None = pydantic.Field(
        None,
        description="Имя пользователя который отправил последнее сообщение",
    )
    fromUserId: int | None = pydantic.Field(
        None,
        description="Идентификатор пользователя который отправил последнее сообщение",
    )
    type: str | None = pydantic.Field(
        None,
        description="Тип посленего соощения",
    )
    time: int | None = pydantic.Field(
        None,
        description="Время отправки последнего сообщения",
    )
    message: str | None = pydantic.Field(
        None,
        description="Текст последнего сообщения",
    )
    profilePicture: str | None = pydantic.Field(
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
