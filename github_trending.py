import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size):
    week_ago = datetime.now() - timedelta(weeks=1)
    request_payload = {
        'q': 'created:>{}'.format(week_ago.strftime('%Y-%m-%d')),
        'sort': 'stars',
        'order': 'des'

    }
    github_response = requests.get(
        'https://api.github.com/search/repositories', params=request_payload

    )
    github_repositories = github_response.json()
    return github_repositories['items'][:top_size]


def get_open_issues_amount(repo_owner, repo_name):
    github_response = requests.get(
        'https://api.github.com/repos/{}/{}/issues'.format(
            repo_owner,
            repo_name
        )
    )
    return len(github_response.json())


if __name__ == '__main__':
    top_size = 20
    trending_repositories = get_trending_repositories(top_size)
    for repository in trending_repositories:
        repo_name = repository['name']
        repo_owner = repository['owner']['login']
        repo_url = repository['html_url']
        stars_count = repository['stargazers_count']
        issues_amount = get_open_issues_amount(repo_owner, repo_name)
        print('Repository: {}\nUrl: {}\nIssues: {}\n'.format(
            repo_name,
            repo_url,
            issues_amount
        ))
