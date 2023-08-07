class Game:

    def __init__(self, ranks = 9, files = 9) -> None:
        self.ranks = ranks
        self.files = files
        self.board = [[0 for _ in range(ranks)] for _ in range(files)]


    def notation(self) -> str:

        ranks_dict = {'1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 1, '9': 0}
        rank_notation = {value: rank_key for rank_key, value in ranks_dict.items()}

        files_dict = {'一': 0, '二': 1, '三': 2, '四': 3, '五': 4, '六': 5, '七': 6, '八': 7, '九': 8}
        file_notation = {value: file_key for file_key, value in files_dict.items()}

        return rank_notation[self.ranks] + file_notation[self.files]
    
