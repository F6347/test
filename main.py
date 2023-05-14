from gd.typing import Optional



def rank(self) -> Optional[int]:
  return self.options.get("global_rank")


print(rank('163042523'))
