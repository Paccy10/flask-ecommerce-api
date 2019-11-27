""" Module for pagination helpers """

from flask import request
from .validators import is_positive_integer, raise_validation_error


def validate_pagination_args(**kwargs):
    """ Validates the pagination request params """

    for key, value in kwargs.items():
        if value is not None:
            try:
                arg = int(value)
                if not is_positive_integer(arg):
                    raise_validation_error(
                        f'The {key} must be a positive integer greater than 0')
            except:
                raise_validation_error(
                    f'The {key} must be a positive integer greater than 0')


def get_pagination_params():
    """
        Generates the pagination params
        Args:
            page(int): page number
            limit(int): maximun number of items per page

        Returns:
            dict: page and limit data
    """
    page = request.args.get('page')
    limit = request.args.get('limit')
    validate_pagination_args(page=page, limit=limit)

    if page is None:
        page = 1

    if limit is None:
        limit = 10

    return int(page), int(limit)


def paginate_resource(model, schema):
    """
        Paginate the given resource
        Args:
            model: resource model
            schema: model schema

        Returns:
            dict: paginated data and metadata
    """

    page, limit = get_pagination_params()

    records_query = model.query.paginate(page=page, max_per_page=limit)
    root_url = request.url_root.strip('/')
    path = request.path
    base_url = f'{root_url}{path}'
    current_page_url = request.url
    next_page_url = None
    previous_page_url = None

    if records_query.has_next:
        next_page_url = f'{base_url}?page={records_query.next_num}&limit={limit}'

    if records_query.has_prev:
        previous_page_url = f'{base_url}?page={records_query.prev_num}&limit={limit}'

    current_page_num = records_query.page
    pages_count = records_query.pages
    total_count = records_query.total
    data = schema.dump(records_query.items)
    meta = {
        'current_page': current_page_url,
        'previous_page': previous_page_url,
        'next_page': next_page_url,
        'page': current_page_num,
        'pages_count': pages_count,
        'total_count': total_count
    }

    return data, meta
