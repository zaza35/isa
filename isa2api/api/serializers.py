from flask_restplus import fields
from isa2api.api.restplus import api

session = api.model('Session inforamtion', {
    'id': fields.String(readOnly=True, description='The unique identifier of session'),
    'caller': fields.String(description='Caller number'),
    'called': fields.String(description='Called number'),
    'timestamp': fields.DateTime(description='Session date'),
    'duration': fields.Integer(description='Session duration'),
    'server': fields.String(),
    'info': fields.String(),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of items'),
})

page_of_sessions = api.inherit('Page of data', pagination, {
    'data': fields.List(fields.Nested(session))
})

node = api.model('Node', {
    'id': fields.String(description='Node unique identifier'),
    'label': fields.String(description='Node label'),
    'group': fields.String(description='Node group'),

})
edge = api.model('Edge', {
    'from': fields.String(description='source node identifier'),
    'to': fields.String(description='target node identifier'),
    'label': fields.String(description='Edge label'),
    'value': fields.String(description='Edge value')

})

graphItems = api.model('Graph nodes & edges', {
    'nodes': fields.List(fields.Nested(node)),
    'edges': fields.List(fields.Nested(edge))
})
session_history = api.model('Session steps', {
    'id': fields.String(readOnly=True, description='The unique identifier of session'),
    'nodes': fields.List(fields.Nested(node)),
    'edges': fields.List(fields.Nested(edge))
})
