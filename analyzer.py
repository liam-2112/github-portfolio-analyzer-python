import pandas as pd
import matplotlib.pyplot as plt
from github_api import fetch_repos

def analyze_languages(repos):
    lang_count = {}
    for repo in repos:
        lang = repo.get('language')
        if lang:
            lang_count[lang] = lang_count.get(lang, 0) + 1
    return lang_count

def plot_languages(lang_count):
    pd.Series(lang_count).sort_values().plot(kind='barh')
    plt.title('Most Used Languages')
    plt.show()

if __name__ == '__main__':
    user = input("Enter GitHub username: ")
    repos = fetch_repos(user)
    lang_data = analyze_languages(repos)
    plot_languages(lang_data)