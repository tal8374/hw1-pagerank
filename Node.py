class Node:

    def __init__(self, id):
        self.int_id = int(id)
        self.str_id = id
        self.temp_rank = None
        self.old_rank = 0

    def __str__(self):
        return 'id: ' + self.str_id + '  - rank: ' + str(self.old_rank) + ' - tmp rank: ' + str(self.temp_rank)

    def __repr__(self):
        return 'id: ' + self.str_id + '  - rank: ' + str(self.old_rank) + ' - tmp rank: ' + str(self.temp_rank)
