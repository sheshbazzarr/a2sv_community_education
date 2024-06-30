class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
      sorted_people= sorted(zip(heights,names),key=lambda x: -x[0])
      sorted_name=[name for heights,name in sorted_people]
      return sorted_name
