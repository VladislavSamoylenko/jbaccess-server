from django import template
register = template.Library()


@register.inclusion_tag("tags/person.html", name="person")
def person(entry):
    return {"person": entry}
