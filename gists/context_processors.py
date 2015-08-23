from .models import Gist
from snippets.models import Snippet


def get_lang_theme(request):
        languages = list(lang[1] for lang in Snippet.LANGUAGES)
        themes = list(lang[1] for lang in Gist.TEMPLATES)

        return {
            "languages": languages,
            "themes": themes
        }
