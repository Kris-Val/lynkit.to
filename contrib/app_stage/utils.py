class GitHash:
    _current_git_hash = None

    def get_current(self):
        if self._current_git_hash:
            return self._current_git_hash

        try:
            import git
        except ImportError:
            self._current_git_hash = "no git"
            return self._current_git_hash

        repo = git.Repo()
        self._current_git_hash = repo.head.object.hexsha
        return self._current_git_hash
