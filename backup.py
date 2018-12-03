import json

from git import Repo
from github import Github

org = '<org>'

git = Github('<token>')

git.per_page = 1

git_org = git.get_organization(org)
git_repos = git_org.get_repos('source')

total_count = git_repos.totalCount

def progress(*args):
 print(args, flush=True)

def clone(repo):
  path = './projects/%s/%s' % (org, repo.name) 
  print(path)
  Repo.clone_from(repo.ssh_url, path, progress)

def main ():
  for repo in git_repos:
    clone(repo)
  
if __name__ == '__main__':
  main()
