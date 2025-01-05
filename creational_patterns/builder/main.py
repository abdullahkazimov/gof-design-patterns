from builder import Director, MacbookBuilder, AsusBuilder

director = Director(MacbookBuilder())

director._builder.build_os()
director._builder.build_cpu()
director._builder.build_gpu()

print(director._builder.get_laptop())

director.change_builder(AsusBuilder())

director._builder.build_os()
director._builder.build_cpu()
director._builder.build_gpu()

print(director._builder.get_laptop())