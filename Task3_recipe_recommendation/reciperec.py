
import tkinter as tk

recipes = {
    "Bread Omelette": ["Bread", "Egg"],
    "French Toast": ["Bread", "Egg", "Milk"],
    "Tea": ["Milk", "Water"],
    "noodles": ["noodles", "Water"],
    "Pancake": ["Milk", "Egg", "Flour"],
    "Milkshake": ["Milk", "Sugar"],
    "Sandwich": ["Bread", "Butter", "vegetable"],
    "Coffee": ["Milk", "Coffee"],
    "Cake": ["Egg", "Flour", "Sugar"],
    "Cookies": ["Flour", "Sugar", "Butter"]
}

ingredients = [
    "Bread",
    "Egg",
    "Milk",
    "Water",
    "Flour",
    "Sugar",
    "Butter",
    "Coffee",
    "noodles",
    "vegetable"
]

def find_recipes():

    selected = []

    for ingredient, var in ingredient_vars.items():

        if var.get() == 1:
            selected.append(ingredient)

    result_box.delete("1.0", tk.END)

    found = False

    for recipe, needed in recipes.items():

        matches = 0

        for item in needed:

            if item in selected:
                matches += 1

        percentage = int((matches / len(needed)) * 100)

        if percentage >= 50:

            result_box.insert(
                tk.END,
                f"⭐ {recipe} ({percentage}% match)\n"
            )

            found = True

    if not found:
        result_box.insert(
            tk.END,
            " No matching recipes found."
        )

root = tk.Tk()
root.title(" Recipe Recommendation System")
root.geometry("600x650")
root.configure(bg="#fff0f5")

title = tk.Label(
    root,
    text="Recipe Recommendation System",
    font=("Comic Sans MS", 18, "bold"),
    bg="#fff0f5",
    fg="#c9184a"
)

title.pack(pady=10)

instruction = tk.Label(
    root,
    text="Select the ingredients you have:",
    font=("Arial", 12),
    bg="#fff0f5",
    fg="#6b3e50"
)

instruction.pack()

frame = tk.Frame(root, bg="#fff0f5")
frame.pack()

ingredient_vars = {}

for ingredient in ingredients:

    var = tk.IntVar()

    checkbox = tk.Checkbutton(
        frame,
        text=ingredient,
        variable=var,
        bg="#fff0f5",
        fg="#6b3e50",
        font=("Arial", 11),
        selectcolor="#ffd6e7"
    )

    checkbox.pack(anchor="w")

    ingredient_vars[ingredient] = var

find_button = tk.Button(
    root,
    text="Find Recipes 💕",
    font=("Arial", 12, "bold"),
    bg="#ffb3c6",
    activebackground="#ffc8dd",
    command=find_recipes
)

find_button.pack(pady=15)

result_label = tk.Label(
    root,
    text="found Recipes",
    font=("Comic Sans MS", 14, "bold"),
    bg="#fff0f5",
    fg="#c9184a"
)

result_label.pack()

result_box = tk.Text(
    root,
    height=12,
    width=40,
    font=("Arial", 11),
    bg="#ffe5ec"
)

result_box.pack(pady=10)

root.mainloop()