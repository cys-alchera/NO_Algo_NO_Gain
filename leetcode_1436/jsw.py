class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_city = set()
        destination_city = set()

        for start, dest in paths:
            start_city.add(start)
            destination_city.add(dest)
        return (destination_city - start_city).pop()