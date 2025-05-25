from django.core.management.base import BaseCommand
from main.models import MenuItem
from decimal import Decimal

class Command(BaseCommand):
    help = 'Adds sample menu items to the database'

    def handle(self, *args, **kwargs):
        # Sample menu items
        items = [
            # Starters (12 items)
            {
                'name': 'Garlic Bread',
                'description': 'Crispy bread topped with garlic butter and herbs',
                'price': Decimal('4.99'),
                'category': 'Starters',
                'image': 'menu_items/garlic_bread.jpg'
            },
            {
                'name': 'Caesar Salad',
                'description': 'Fresh romaine lettuce with Caesar dressing, croutons, and parmesan',
                'price': Decimal('6.99'),
                'category': 'Starters',
                'image': 'menu_items/caesar_salad.jpg'
            },
            {
                'name': 'Bruschetta',
                'description': 'Toasted bread topped with tomatoes, garlic, and fresh basil',
                'price': Decimal('5.99'),
                'category': 'Starters',
                'image': 'menu_items/bruschetta.jpg'
            },
            {
                'name': 'Mozzarella Sticks',
                'description': 'Crispy breaded mozzarella sticks served with marinara sauce',
                'price': Decimal('7.99'),
                'category': 'Starters',
                'image': 'menu_items/mozzarella_sticks.jpg'
            },
            {
                'name': 'Calamari',
                'description': 'Crispy fried calamari rings with lemon and cocktail sauce',
                'price': Decimal('9.99'),
                'category': 'Starters',
                'image': 'menu_items/calamari.jpg'
            },
            {
                'name': 'Spinach Dip',
                'description': 'Creamy spinach and artichoke dip served with tortilla chips',
                'price': Decimal('8.99'),
                'category': 'Starters',
                'image': 'menu_items/spinach_dip.jpg'
            },
            {
                'name': 'Wings',
                'description': 'Chicken wings with choice of buffalo, BBQ, or honey garlic sauce',
                'price': Decimal('10.99'),
                'category': 'Starters',
                'image': 'menu_items/wings.jpg'
            },
            {
                'name': 'Shrimp Cocktail',
                'description': 'Chilled shrimp served with cocktail sauce and lemon',
                'price': Decimal('11.99'),
                'category': 'Starters',
                'image': 'menu_items/shrimp_cocktail.jpg'
            },
            {
                'name': 'Nachos',
                'description': 'Tortilla chips topped with cheese, jalapeños, and salsa',
                'price': Decimal('8.99'),
                'category': 'Starters',
                'image': 'menu_items/nachos.jpg'
            },
            {
                'name': 'Soup of the Day',
                'description': 'Chef\'s special soup made fresh daily',
                'price': Decimal('5.99'),
                'category': 'Starters',
                'image': 'menu_items/soup.jpg'
            },
            {
                'name': 'Stuffed Mushrooms',
                'description': 'Mushroom caps stuffed with cheese and herbs',
                'price': Decimal('7.99'),
                'category': 'Starters',
                'image': 'menu_items/stuffed_mushrooms.jpg'
            },
            {
                'name': 'Spring Rolls',
                'description': 'Crispy vegetable spring rolls with sweet chili sauce',
                'price': Decimal('6.99'),
                'category': 'Starters',
                'image': 'menu_items/spring_rolls.jpg'
            },

            # Main Courses (12 items)
            {
                'name': 'Grilled Salmon',
                'description': 'Fresh salmon fillet grilled to perfection with lemon butter sauce',
                'price': Decimal('18.99'),
                'category': 'Main Courses',
                'image': 'menu_items/grilled_salmon.jpg'
            },
            {
                'name': 'Beef Steak',
                'description': 'Premium beef steak cooked to your preference with mushroom sauce',
                'price': Decimal('24.99'),
                'category': 'Main Courses',
                'image': 'menu_items/beef_steak.jpg'
            },
            {
                'name': 'Chicken Alfredo',
                'description': 'Fettuccine pasta with creamy Alfredo sauce and grilled chicken',
                'price': Decimal('16.99'),
                'category': 'Main Courses',
                'image': 'menu_items/chicken_alfredo.jpg'
            },
            {
                'name': 'Vegetable Lasagna',
                'description': 'Layers of pasta, vegetables, and cheese in tomato sauce',
                'price': Decimal('15.99'),
                'category': 'Main Courses',
                'image': 'menu_items/vegetable_lasagna.jpg'
            },
            {
                'name': 'Fish and Chips',
                'description': 'Beer-battered fish with crispy fries and tartar sauce',
                'price': Decimal('17.99'),
                'category': 'Main Courses',
                'image': 'menu_items/fish_and_chips.jpg'
            },
            {
                'name': 'Chicken Curry',
                'description': 'Tender chicken in aromatic curry sauce with rice',
                'price': Decimal('16.99'),
                'category': 'Main Courses',
                'image': 'menu_items/chicken_curry.jpg'
            },
            {
                'name': 'Beef Burger',
                'description': 'Juicy beef patty with cheese, lettuce, and special sauce',
                'price': Decimal('14.99'),
                'category': 'Main Courses',
                'image': 'menu_items/beef_burger.jpg'
            },
            {
                'name': 'Pork Chops',
                'description': 'Grilled pork chops with apple sauce and vegetables',
                'price': Decimal('19.99'),
                'category': 'Main Courses',
                'image': 'menu_items/pork_chops.jpg'
            },
            {
                'name': 'Seafood Pasta',
                'description': 'Pasta with mixed seafood in white wine sauce',
                'price': Decimal('21.99'),
                'category': 'Main Courses',
                'image': 'menu_items/seafood_pasta.jpg'
            },
            {
                'name': 'Vegetable Stir Fry',
                'description': 'Assorted vegetables stir-fried in soy sauce with rice',
                'price': Decimal('15.99'),
                'category': 'Main Courses',
                'image': 'menu_items/stir_fry.jpg'
            },
            {
                'name': 'Lamb Shank',
                'description': 'Slow-cooked lamb shank with red wine sauce',
                'price': Decimal('23.99'),
                'category': 'Main Courses',
                'image': 'menu_items/lamb_shank.jpg'
            },
            {
                'name': 'Chicken Parmesan',
                'description': 'Breaded chicken topped with marinara sauce and cheese',
                'price': Decimal('17.99'),
                'category': 'Main Courses',
                'image': 'menu_items/chicken_parmesan.jpg'
            },

            # Desserts (12 items)
            {
                'name': 'Chocolate Cake',
                'description': 'Rich chocolate cake with chocolate ganache',
                'price': Decimal('7.99'),
                'category': 'Desserts',
                'image': 'menu_items/chocolate_cake.jpg'
            },
            {
                'name': 'Tiramisu',
                'description': 'Classic Italian dessert with coffee-soaked ladyfingers and mascarpone cream',
                'price': Decimal('8.99'),
                'category': 'Desserts',
                'image': 'menu_items/tiramisu.jpg'
            },
            {
                'name': 'Ice Cream Sundae',
                'description': 'Vanilla ice cream with chocolate sauce, whipped cream, and nuts',
                'price': Decimal('6.99'),
                'category': 'Desserts',
                'image': 'menu_items/ice_cream.jpg'
            },
            {
                'name': 'Cheesecake',
                'description': 'Creamy New York style cheesecake with berry compote',
                'price': Decimal('7.99'),
                'category': 'Desserts',
                'image': 'menu_items/cheesecake.jpg'
            },
            {
                'name': 'Apple Pie',
                'description': 'Warm apple pie with vanilla ice cream',
                'price': Decimal('6.99'),
                'category': 'Desserts',
                'image': 'menu_items/apple_pie.jpg'
            },
            {
                'name': 'Crème Brûlée',
                'description': 'Classic French vanilla custard with caramelized sugar top',
                'price': Decimal('8.99'),
                'category': 'Desserts',
                'image': 'menu_items/creme_brulee.jpg'
            },
            {
                'name': 'Chocolate Mousse',
                'description': 'Light and airy chocolate mousse with whipped cream',
                'price': Decimal('7.99'),
                'category': 'Desserts',
                'image': 'menu_items/chocolate_mousse.jpg'
            },
            {
                'name': 'Fruit Tart',
                'description': 'Buttery pastry filled with custard and fresh fruits',
                'price': Decimal('8.99'),
                'category': 'Desserts',
                'image': 'menu_items/fruit_tart.jpg'
            },
            {
                'name': 'Bread Pudding',
                'description': 'Warm bread pudding with vanilla sauce',
                'price': Decimal('6.99'),
                'category': 'Desserts',
                'image': 'menu_items/bread_pudding.jpg'
            },
            {
                'name': 'Panna Cotta',
                'description': 'Italian vanilla cream dessert with berry sauce',
                'price': Decimal('7.99'),
                'category': 'Desserts',
                'image': 'menu_items/panna_cotta.jpg'
            },
            {
                'name': 'Chocolate Fondant',
                'description': 'Warm chocolate cake with molten center',
                'price': Decimal('8.99'),
                'category': 'Desserts',
                'image': 'menu_items/chocolate_fondant.jpg'
            },
            {
                'name': 'Lemon Tart',
                'description': 'Tangy lemon curd in sweet pastry shell',
                'price': Decimal('7.99'),
                'category': 'Desserts',
                'image': 'menu_items/lemon_tart.jpg'
            },

            # Fine Wines (12 items)
            {
                'name': 'Chardonnay',
                'description': 'Premium white wine with notes of oak and vanilla',
                'price': Decimal('12.99'),
                'category': 'Fine Wines',
                'image': 'menu_items/chardonnay.jpg'
            },
            {
                'name': 'Merlot',
                'description': 'Smooth red wine with rich berry flavors',
                'price': Decimal('14.99'),
                'category': 'Fine Wines',
                'image': 'menu_items/merlot.jpg'
            },
            {
                'name': 'Prosecco',
                'description': 'Italian sparkling wine, perfect for celebrations',
                'price': Decimal('11.99'),
                'category': 'Fine Wines',
                'image': 'menu_items/prosecco.jpg'
            },
            {
                'name': 'Cabernet Sauvignon',
                'description': 'Full-bodied red wine with blackcurrant notes',
                'price': Decimal('15.99'),
                'category': 'Fine Wines',
                'image': 'menu_items/cabernet.jpg'
            },
            {
                'name': 'Pinot Grigio',
                'description': 'Light and crisp white wine with citrus notes',
                'price': Decimal('13.99'),
                'category': 'Fine Wines',
                'image': 'menu_items/pinot_grigio.jpg'
            },
            {
                'name': 'Malbec',
                'description': 'Rich red wine with plum and chocolate notes',
                'price': Decimal('14.99'),
                'category': 'Fine Wines',
                'image': 'menu_items/malbec.jpg'
            },
            {
                'name': 'Sauvignon Blanc',
                'description': 'Refreshing white wine with tropical fruit notes',
                'price': Decimal('12.99'),
                'category': 'Fine Wines',
                'image': 'menu_items/sauvignon_blanc.jpg'
            },
            {
                'name': 'Shiraz',
                'description': 'Bold red wine with spicy and dark fruit flavors',
                'price': Decimal('15.99'),
                'category': 'Fine Wines',
                'image': 'menu_items/shiraz.jpg'
            },
            {
                'name': 'Rosé',
                'description': 'Light and fruity pink wine, perfect for summer',
                'price': Decimal('11.99'),
                'category': 'Fine Wines',
                'image': 'menu_items/rose.jpg'
            },
            {
                'name': 'Pinot Noir',
                'description': 'Elegant red wine with cherry and earthy notes',
                'price': Decimal('16.99'),
                'category': 'Fine Wines',
                'image': 'menu_items/pinot_noir.jpg'
            },
            {
                'name': 'Riesling',
                'description': 'Sweet white wine with floral and honey notes',
                'price': Decimal('13.99'),
                'category': 'Fine Wines',
                'image': 'menu_items/riesling.jpg'
            },
            {
                'name': 'Zinfandel',
                'description': 'Fruity red wine with jammy berry flavors',
                'price': Decimal('14.99'),
                'category': 'Fine Wines',
                'image': 'menu_items/zinfandel.jpg'
            }
        ]

        # Create menu items
        for item_data in items:
            MenuItem.objects.get_or_create(
                name=item_data['name'],
                defaults={
                    'description': item_data['description'],
                    'price': item_data['price'],
                    'category': item_data['category'],
                    'image': item_data['image']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully added sample menu items')) 