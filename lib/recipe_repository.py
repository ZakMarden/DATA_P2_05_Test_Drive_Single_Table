from lib.recipe import Recipe

class RecipeRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM recipes")
        return [Recipe(row["id"], row["name"], row["average_cooking_time"], row["rating"]) for row in rows]
    
    def find(self, id):
        recipe = self._connection.execute(f"SELECT * FROM recipes WHERE id = {id}")[0]
        return Recipe(recipe["id"], recipe["name"], recipe["average_cooking_time"], recipe["rating"])