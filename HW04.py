'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-02-16 17:25:56
'''
import urllib.request
import json



def search_repo(user_id):
    '''  search repository name and its commits'''
    
    URL = f"https://api.github.com/users/{user_id}/repos"
    
    repo = urllib.request.Request(URL)
    
    fhand = urllib.request.urlopen(repo).read().decode()
    
    js_str = json.loads(fhand)
    
    n = len(js_str)

    commits_num={}

    for i in range(n):

        repo_name = js_str[i]["name"]
        
        URL = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        
        commits = urllib.request.Request(URL)
        
        fhand_commit = urllib.request.urlopen(commits).read().decode()
        
        js_str_commit = json.loads(fhand_commit)
        
        commits_num[repo_name]=len(js_str_commit)

    return commits_num


def main():
    commit=search_repo("JamesLi0217")
    for repo in commit:
        print(f"Repo: {repo} Number of commits: {commit[repo]}")


if __name__ == "__main__":
    main()
    
    
    