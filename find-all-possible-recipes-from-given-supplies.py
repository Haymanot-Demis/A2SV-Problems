class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        color = [0] * len(recipes)
        name_to_key = defaultdict(lambda : None) 
        for indx, recipe in enumerate(recipes):
            name_to_key[recipe] = indx
        
        supplies = set(supplies)
        answer = []

        for indx, recipe in enumerate(recipes):
            result = self.dfs(recipe, ingredients, supplies, name_to_key, color)
            if result:
                answer.append(recipe)

        return answer

    def dfs(self, ingredient, ingredients, supplies, name_to_key, color):
        if ingredient in supplies:
            return True
        
        if ingredient not in name_to_key:
            return False

        indx = name_to_key[ingredient]

        if color[indx] == 1:
            return False

        color[indx] = 1
        for ingredient in ingredients[indx]:
            if not self.dfs(ingredient, ingredients, supplies, name_to_key, color):
                return False
        
        supplies.add(ingredient)
        color[indx] = 2
        return True