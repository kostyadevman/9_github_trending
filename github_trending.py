import requests


def get_trending_repositories(top_size):
    github_response = requests.get(
        'https://api.github.com/search/repositories?q=created:%3E2018-03-01&sort=stars&order=des'
    )
    github_repositories = github_response.json()
    return github_repositories['items'][:top_size]


def get_open_issues_amount(repo_owner, repo_name):
    github_response = requests.get(
        'https://api.github.com/repos/{}/{}/issues'.format(
            repo_name,
            repo_owner
        )
    )
    return len(github_response.json())


if __name__ == '__main__':
    top_size = 2
    trending_repositories = get_trending_repositories(top_size)
    for repository in trending_repositories:
        repo_name = repository['name']
        repo_owner = repository['owner']['login']
        repo_url = repository['html_url']
        stars_count = repository['stargazers_count']
        issues_amount = get_open_issues_amount(repo_owner, repo_name)

