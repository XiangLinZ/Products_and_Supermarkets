listadia1 = ["conservas" ,"dieteticos"]
listadia2 = ["alinos", "tomate", "levaduras", "biscotes", "tartaletas", "pates", "almibar", "pures", "nata", "horno", "cremas", "margarina", "esponjas", "caldos", "sopas", "hojaldres", "foies"]
listacategorias_merc = [27, 28, 29, 32, 33, 34, 36, 37, 38, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 58, 59, 60, 62, 64, 65, 66, 68, 69, 71, 72, 75, 77, 78, 79,
                80, 81, 83, 84, 86, 88, 89, 90, 92, 95, 97, 98, 99, 100, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 115, 116, 117, 118, 120, 121, 122, 123, 126, 127, 129,
                130, 132, 133, 135, 138, 140, 142, 143, 145, 147, 148, 149, 150, 151, 152, 154, 155, 156, 158, 159, 161, 162, 163, 164, 166, 168, 169, 170, 171, 173, 174, 181, 185,
                186, 187, 188, 189, 190, 191, 192, 194, 196, 198, 199, 201, 202, 203, 205, 206, 207, 208, 210, 212, 213, 214, 216, 217, 218, 219, 221, 222, 225, 226, 229, 230, 231,
                232, 233, 234, 235, 237, 238, 239, 241, 243, 244, 782, 789, 884]
categoria_n_dia = ["dulces-de-navidad", "platos-preparados", "frescos", "despensa", "bebidas", "bodega", "congelados", "cuidado-personal", "bebe", "cuidado-del-hogar", "mascotas"]

productos_mercadona_estructura = {"name": [], "category": [], "price": [], "reference_price": [], "reference_unit": [], "insert_date": [], "category_id":[]}
dia_cuid = {
    "sexual" : "intimo", "alimentos" : "cocina", "afeitado" : "depilacion", "papel": "hogar",
    "ambientadores" : "ambientadores_insecticidas", "insecticidas" : "ambientadores_insecticidas",
    "champus": "cabello", "pies": "corporal", "desodorantes": "colonias", "jabon": "gel_jabones", "gel": "gel_jabones",
    "horno": "pan", "cremas": "precocinados", "tomate": "salsas", "levaduras": "harinas",
    "margarina": "mantequilla", "almibar" : "conservas", "pures": "precocinados", "nata": "leche",
    "pates": "conservas", "tartaletas": "reposteria", "biscotes" : "pan_tostado",
    "alinos": "vinagre", "esponjas" : "gel_jabones", "caldos": "precocinados", "sopas": "precocinados",
    "hojaldres": "reposteria", "foies": "conservas"}
dia_con = {
    "helados" : ["helado", "nata", "granizados", "bloques", "postres", "bombones", "tarrinas", "sandwich","helados", "conos", "polos"],
    "pescaderia_cong" : ["cefalopodos", "marisco", "gulas", "pescado"],
    "vegetales_cong" : ["guisantes", "hortalizas", "patatas","simples", "condimentos", "acelgas", "vegetales"],
    "carnes_cong" : ["pollo", "carne", "carnes"],
    "precocinados_cong" : ["preparados", "preparado", "caldo", "precocinados", "salteados", "pasta", "croquetas", "empanadillas", "ensaladillas", "masas", "reposteria", "porras"],
    "hielo" : ["hielo", "hielos"]}
dia_bebis = {
    "refrescos" : ["refrescos", "cola", "refrigerados", "limon", "ale", "frutas", "naranja", "te", "sodas", "limalimon", "bitter", "preparar"],
    "zumos": ["zumos", "zumo", "nectar", "mosto", "exprimido"],
    "cervezas": ["especiales", "nacionales", "especialidades", "premium", "light", "sabores", "sidra", "estandar", "alcohol"],
    "isotonicas_energeticas": ["isotonicas", "energeticas"],
    "agua": ["aguas", "gas"],
    "leche" : ["horchata"],
    "destilados_licores": ["ginebra", "boubon", "ron", "cognac", "manzanilla", "vodka", "aperitivos", "moscatel", "fino", "licor", "semiseco", "nature", "anis", "ponche", "brut", "cremas", "bourbon"],
    "sangrias" : ["vinos", "vino"]}
dia_bode = {
    "destilados_licores" : ["whiskey", "ron", "vermouth", "ginebra", "vodka", "dulce", "espumosos", "whisky", "brandy", "cremas", "hierbas", "anis", "licores", "alcohol", "pacharan"],
    "vino_tinto": ["tinto"],
    "vino_blanco": ["blanco"],
    "vino_rosado": ["rosado"],
    "sangrias": ["verano"]}
dia_be = {
    "higiene": ["toallitas", "puericultura", "champu", "infantil", "lociones", "jabon", "bebe"],
    "alimentacion": ["bebes", "legumbres", "infantiles", "yogures", "papillas", "postre", "carne", "polvo", "bebidas", "pescado", "liquidas", "tarritos"],
    "panales": ["panales", "banadores", "aprendizaje", "kg"]}
dia_fre = {
    "quesos": ["quesos", "curados"],
    "aves": ["pavo", "pollo", "aves"],
    "vacuno": ["vacuno", "ternera"],
    "cerdo" : ["cerdo"],
    "conejo_cordero": ["conejo", "cordero"],
    "elaborados": ["elaborados", "adobados"],
    "embutidos": ["cocidos", "morcilla", "sobrasadas"],
    "picados": ["mixto", "picadas"],
    "pescado": ["azul", "fresco", "salazones", "marinados" ,"corte", "blanco"],
    "marisco": ["fresco", "marisco", "surimi", "derivados", "especialidades", "sepia"],
    "fruta": ["fruta", "bosque", "platanos", "manzanas", "citricos", "tropicales", "tropical", "pepino", "peras", "pera", "tomates", "citricos", "uvas", "temporada", "banana", "uva", "frutas", "pepinos"],
    "vegetales": ["puerro", "guisantes", "boniatos", "coliflor", "coliflores", "endivia", "puerros", "alcachofas", "calabacin","zanahorias", "pimiento", "raices", "alcachofa", "verduras", "endibias","algas", "espinacas", "endivias", "berenjena"],
    "hongos": ["champinones", "setas", "seta", "esparragos"],
    "precocinados" : ["preparados", "cocinados", "consumir", "cocinadas", "preparadas"],
    "especias" : ["aromaticas"]}
dia_per = {
    "cabello": ["cabello", "champu", "coloracion", "fijadores", "suavizante"],
    "gel_jabones": ["bano", "pastilla", "accesorios", "liquido"],
    "corporal": ["crema", "milk", "manos", "aceite", "anticelulitis", "anticeluliticos"],
    "bucal": ["dentifrico", "dientes", "dental", "antiseptico", "protesicos", "dentifricos", "antisepticos"],
    "colonias": ["spray", "desodorante", "familiar", "on", "femeninas", "masculinas", "barra"],
    "facial": ["antiedad", "exfoliante", "nutritivas", "limpiadores", "labial", "especificas", "especificos"],
    "cosmetica": ["desmaquilladores", "cosmetica", "ojos"],
    "depilacion": ["afeitar", "recambio", "afeitado", "cera", "bandas", "desechables", "recambios"],
    "solar": ["solar", "sol"],
    "intimo" : ["slips", "compresas", "tampones", "incontinencia", "preservativos", "lubricantes", "intimo"],
    "botiquin": ["otros", "bastoncitos", "optica", "protectoras", "mascarillas", "bastoncillos", "bicarbonato"]}
dia_lac = {
    "yogures": ["desnatado", "bifidus", "griego", "lcasei", "sabores", "infantiles", "liquido", "frutas", "liquidos","natural", "soja"],
    "leche": ["semidesnatada", "deshidratada", "entera", "desnatada", "calcio", "lactosa", "especiales", "cocinar", "montar", "condensada", "enriquecidos"],
    "batidos": ["horchatas", "cacao", "vainilla", "fresa"],
    "postres": ["natillas", "flan", "gelatina", "postres", "mousse", "crema", "copa", "cuajada", "leche", "tartas"],
    "huevos": ["medianos", "grandes"],
    "mantequilla": ["mantequilla", "margarina"]}
dia_des = {
    "chocolate": ["chocolatinas", "chocolate", "tabletas", "adviento"],
    "cacao": ["cacao", "taza", "instantaneo"],
    "dulces": ["golosinas", "chicles", "duros", "turrones", "mazapanes", "polvorones", "navidenos", "navidad"],
    "cafe": ["mezcla", "natural", "capsulas", "descafeinado", "grano", "otros"],
    "bolleria": ["productos", "donuts", "magdalenas", "napolitanas", "bizcochos", "campana", "reyes", "panettones", "rosquillas"],
    "infusiones": ["poleo", "tila", "terapeuticos", "te", "manzanilla", "infusiones", "terapeuticas"],
    "galletas": ["rellenas", "salud", "digestive", "maria", "barquillos", "desayuno", "infantil"],
    "reposteria": ["caramelos", "postres", "tartaletas"],
    "cereales": ["cereales", "muesli", "infantiles", "familiar", "achicoria"],
    "pan": ["bocadillos", "hornear", "fresco", "brioches"],
    "pan_tostado": ["tostado", "tostados", "picatostes", "aperitivo"],
    "vinagre": ["alinos"],
    "postres": ["gelatinas", "gelatina", "natillas"],
    "edulcorantes": ["edulcorantes", "azucar"],
    "molde": ["integral", "blanco"],
    "rallado": ["rallado"], 
    "bombones": ["bombones"],
    "mantequilla":["mantequilla"]}
dia_dro = {
    "ropa" : ["ropa", "comun", "liquido", "delicadas", "gamuzas", "quitamanchas", "concentrado", "tabletas", "polvo", "lavado", "diluido"],
    "limpieza": ["cristales", "fregonas", "especifico", "destilada", "estropajos", "multiusos", "lejia", "quitagrasas", "vitroceramica", "madera", "antical", "muebles", "metales", "suelos", "fregasuelos"],
    "ambientadores_insecticidas": ["spray", "antihumedad", "repelentes", "voladores", "automaticos", "decorativos", "carcoma", "caminantes", "electricos", "pequenos"],
    "bano": ["banos", "wc", "tuberias"],
    "lavavajillas" : ["mano", "lavavajillas", "pastillas"],
    "hogar": ["pilas", "higienico", "basura", "papel", "bombillas", "humedo", "tissue","guantes", "plumero", "tapicerias", "plantas", "tissues", "reutilizables"],
    "calzado" :["limpiacalzado", "calzado"],
    "cocina": ["cocina", "mecheros", "transparente", "aluminio", "congelar", "horno", "conservacion", "desechables", "pajitas", "cafe"],
    "bazar": ["bazar", "objeto"]}
dia_charc = {
    "quesos" : ["fundidos", "light", "rallados", "semicurados", "curados", "ensaladas", "oveja", "untar", "corte", "cabra", "maasdam", "roquefort", "gruyere", "cremosos", "barra", "importacion"],
    "conservas": ["pates", "foie"], 
    "embutidos": ["jamon", "ave", "embutidos", "chopped", "panceta", "salami", "lomo", "chorizo", "york", "tablas", "longaniza", "salchichas", "sobrasada"]}
dia_alim = {
    "especias": ["especias", "sal", "sazonadores"],
    "aperitivos": ["aperitivos", "verdes", "negras", "saladas", "secos", "fritas", "rellenas", "encurtidos"],
    "mayonesa": ["mayonesa"],
    "vinagre": ["vinagre"],
    "ketchup": ["ketchup"],
    "mostaza": ["mostaza"],
    "salsas": ["limon", "otras", "bechamel", "salsas", "preparar", "rosa", "pastas", "oli", "soja", "frito"],
    "aceites": ["06o1o", "05o", "extra", "girasol", "aceites"],
    "precocinados_cong": ["congelada", "congeladas"],
    "dieteticos": ["deportistas", "peso", "nutricionales", "tortitas"],
    "conservas": ["conservas", "esparrago", "ventresca", "almejas", "tomate", "guisante", "sardinillas", "berberechos", "vegetales", "mejillones", "menestras", "jugo", "maiz", "ensaladas", "compotas", "carne", "alcachofa", "pulpo", "verde", "champinones", "espinacas", "anchoas", "caballa"],
    "arroz" : ["arroz", "redondo", "vaporizado", "largo", "cocido", "semolas"],
    "precocinados" : ["preparada", "pastillas", "lasanas", "sobre", "patata", "brick", "refrigeradas", "ensalada", "preparadas"],
    "pastas" : ["fresca", "tallarines", "sopa", "corta"],
    "harinas" : ["harinas", "levaduras"],
    "vegetales": ["pimiento"],
    "legumbres": ["cocidas", "cocidos", "preparadas", "garbanzos", "lentejas", "alubias"]}
diccategoria = {
    "bebidas": ["isotonicas_energeticas", "refrescos", "agua", "zumos"],
    "precocinados": ["precocinados"],
    "alcoholicas": ["vinos_tintos", "destilados_licores", "cervezas", "vinos_blancos", "vinos_rosados", "sangrias"],
    "mascotas": ["otros", "gatos", "perros", "accesorios"],
    "desayunos": ["cereales", "galletas", "bolleria", "cafe", "cacao", "infusiones"],
    "despensa": ["ketchup", "conservas", "harinas", "pastas", "especias", "salsas", "mayonesa", "mostaza", "aceites", "reposteria", "edulcorantes", "legumbres", "arroz", "vinagre","raro"],
    "pan": ["pan_tostado", "molde", "pan", "rallado", "perritos"],
    "snacks" : ["golosinas", "bombones", "aperitivos", "chocolate", "dulces"],
    "huevos_lacteos_derivados": ["leche", "yogures", "postres", "huevos", "mantequilla", "queso", "batidos"],
    "internacional": ["mejicana", "oriental", "otras"],
    "congelados": ["precocinados_cong", "pescaderia_cong", "carnes_cong", "vegetales_cong", "hielo", "helados"],
    "carniceria": ["embutidos", "aves", "vacuno", "cerdo", "picados", "elaborados", "conejo_cordero"],
    "pescaderia": ["pescado", "marisco"],
    "verduleria" : ["vegetales", "hongos", "fruta"],
    "cuidado_higiene_personal": ["corporal", "cosmetica", "facial", "gel_jabones", "solar", "cabello", "dieteticos", "colonias", "intimo", "bucal", "botiquin", "depilacion"],
    "cuidado_higiene_hogar": ["bano", "hogar", "cocina", "ropa", "limpieza", "lavavajillas", "ambientadores_insecticidas", "calzado", "bazar"],
    "bebe": ["panales", "alimentacion", "higiene"]}
mer_cuid = {
    "zumos": "zumos", "fitoterapia": "botiquin", "pizzas": "precocinados","aperitivos": "aperitivos", "maquillaje": "cosmetica"}
mer_con = {
    "helados": ["helados"],
    "vegetales_cong": ["verdura"], 
    "pescaderia_cong": ["pescado", "marisco"],
    "precocinados_cong": ["churros", "rebozados", "pizzas", "pasta"],
    "hielo": ["hielo"],
    "carnes_cong" : ["carne"]}
mer_charc = {
    "queso" : ["fresco", "curado", "tierno", "porciones"],
    "embutidos": ["cocido", "serrano", "sobrasada", "salchichas", "mortadela"]}
mer_pan = {
    "pan": ["horno"],
    "bolleria": ["envasada", "pasteles"],
    "harinas": ["reposteria"],
    "molde": ["especialidades"],
    "rallado" : ["rallado"],
    "pan_tostado": ["picatostes"],
    "reposteria": ["decoracion", "repostería"]}
mer_cui = {
    "colonias": ["colonia", "desodorante"],
    "cabello": ["cabello", "mascarilla", "accesorios", "champu"],
    "intimo": ["intima"],
    "facial": ["facial"],
    "bucal": ["bucal"],
    "corporal": ["corporal", "pedicura", "neceseres"],
    "gel_jabones": ["manos"],
    "depilacion": ["hombre", "depilacion"],
    "solar": ["aftersun"]}
mer_hue = {
    "leche": ["vegetales"],
    "mantequilla": ["margarina"],
    "huevos" : ["huevos"]}
mer_azuc = {
    "chocolate": ["chocolate"],
    "dulces": ["caramelos", "turrones"],
    "conservas": ["miel"],
    "golosinas": ["golosinas"],
    "edulcorantes": ["edulcorante"]}
mer_bod = {
    "cervezas": ["cerveza", "cava", "alcohol"],
    "destilados_licores": ["licores", "espumoso"],
    "vinos_tintos": ["tinto"],
    "vinos_blancos": ["blanco"],
    "vinos_rosados": ["rosado"],
    "sangrias": ["sangria"]}
mer_frut = {
    "vegetales": ["verdura"],
    "fruta": ["fruta"],
    "precocinados": ["preparada"]}
mer_lim = {
    "ambientadores_insecticidas": ["ambientador"],
    "calzado": ["calzado"],
    "ropa": ["ropa"],
    "cocina":["alimentos", "cocina"],
    "hogar": ["guantes", "basura", "celulosa"],
    "limpieza": ["fuertes", "multiusos", "friegasuelos", "limpiacristales"],
    "bano": ["wc"],
    "lavavajillas": ["vajilla"]}
mer_cer = {
    "galletas": ["galletas", "tortitas"],
    "cereales": ["cereales"]}
mer_arr = {
    "pastas": ["fideos"],
    "legumbres": ["legumbres"],
    "arroz": ["arroz"]}
mer_bebe = {
    "alimentacion": ["infantil", "menaje"],
    "panales": ["panales"],
    "higiene" : ["cuidado"]}
mer_cons = {
    "conservas": ["frutas", "pescado", "mejillones"],
    "precocinados": ["caldo", "cremas", "tomate"]}
mer_masc = {
    "perros": ["perro"],
    "gatos": ["gato"],
    "otros": ["otros"]}
mer_car = {
    "aves": ["pollo"],
    "cerdo": ["cerdo"],
    "picados": ["picadas"],
    "vacuno": ["vacuno"],
    "elaborados": ["elaborados"],
    "carnes_cong": ["congeladas", "congelada"],
    "embutidos": ["embutidos", "arreglos", "embutido"],
    "conejo_cordero" : ["cordero"]}
mer_mari = {
    "pescado" : ["fresco", "bandeja", "ahumados"],
    "precocinados": ["sushi"],
    "marisco": ["marisco"],
    "pescaderia_cong": ["congelado"]}
mer_acei = {
    "especias": ["especias"],
    "salsas": ["salsas"],
    "raro" : ["sal", "mostaza"]}
mer_agua = {
    "agua": ["agua"],
    "refrescos": ["cola", "limon", "gas", "bitter"],
    "isotonicas_energeticas": ["energetico"]}
mer_cac = {
    "cafe": ["monodosis", "bebidas", "grano"],
    "infusiones": ["infusiones"],
    "cacao": ["taza"]}
mer_post = {
    "yogures": ["liquidos", "bifidus", "sabores", "desnatados", "griegos", "infantiles", "líquidos", "bífidus"],
    "postres": ["postres", "natillas", "soja"]}
diccategoria = {
    "bebidas": ["isotonicas_energeticas", "refrescos", "agua", "zumos"],
    "precocinados": ["precocinados"],
    "alcoholicas": ["vinos_tintos", "destilados_licores", "cervezas", "vinos_blancos", "vinos_rosados", "sangrias"],
    "mascotas": ["otros", "gatos", "perros", "accesorios"],
    "desayunos" : ["cereales", "galletas", "bolleria", "cafe", "cacao", "infusiones"],
    "despensa" : ["ketchup", "conservas", "harinas", "pastas", "especias", "salsas", "mayonesa", "mostaza", "aceites", "reposteria", "edulcorantes", "legumbres", "arroz", "vinagre","raro"],
    "pan" : ["pan_tostado", "molde", "pan", "rallado", "perritos"],
    "snacks" : ["golosinas", "bombones", "aperitivos", "chocolate", "dulces"],
    "huevos_lacteos_derivados": ["leche", "yogures", "postres", "huevos", "mantequilla", "queso", "batidos"],
    "internacional": ["mejicana", "oriental", "otras"],
    "congelados": ["precocinados_cong", "pescaderia_cong", "carnes_cong", "vegetales_cong", "hielo", "helados"],
    "carniceria": ["embutidos", "aves", "vacuno", "cerdo", "picados", "elaborados", "conejo_cordero"],
    "pescaderia": ["pescado", "marisco"],
    "verduleria" : ["vegetales", "hongos", "fruta"],
    "cuidado_higiene_personal": ["corporal", "cosmetica", "facial", "gel_jabones", "solar", "cabello", "dieteticos", "colonias", "intimo", "bucal", "botiquin", "depilacion"],
    "cuidado_higiene_hogar": ["bano", "hogar", "cocina", "ropa", "limpieza", "lavavajillas", "ambientadores_insecticidas", "calzado", "bazar"],
    "bebe": ["panales", "alimentacion", "higiene"]}
