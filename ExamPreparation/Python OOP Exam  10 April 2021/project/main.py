from project.controller import Controller

controller = Controller()
print(controller.add_aquarium("FreshwaterAquarium", "Test"))
print(controller.add_aquarium("FreshwaterAquarium", "Test1"))

print(controller.aquariums)
print(controller.add_decoration("Plant1"))
print(controller.decorations_repository)
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Plant"))

print(controller.decorations_repository.decorations)
print(controller.insert_decoration("Test", "Plant"))
print(controller.decorations_repository.decorations)
print(controller.add_fish("Test", "FreshwaterFish", "test_fish", "specie", 10))
print(controller.add_fish("Test", "FreshwaterFish", "test_fish1", "specie", 10))
print(controller.add_fish("Test", "FreshwaterFish", "test_fish2", "specie", 10))

print(controller.feed_fish("Test"))
print(controller.calculate_value("Test"))
print(controller.report())
