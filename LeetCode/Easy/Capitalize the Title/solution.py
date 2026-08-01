class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        result = []
        for val in words:
            if len(val)==1 or len(val)==2:
                result.append(val.lower())
            else:
                result.append(val.title())

        return " ".join(result)

        