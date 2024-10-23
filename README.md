# data-collection-json-csv-sql
data-collection-json-csv-sql is a repository dedicated to storing a variety of datasets in both JSON, SQL and CSV formats. This collection includes data from different domains and can be used for data analysis, machine learning projects, or educational purposes.

# Crear bases de datos
```mongodb
use test_db;  // Cambia el contexto de la base de datos a 'test_db'
```
<img src="images\01_create_database.png">

# Crear una coleccion
```mongodb
db.createCollection('test_collection');  // Crea una nueva colección llamada 'test_collection' en la base de datos actual
// { ok: 1 }  // Mensaje de confirmación que indica que la colección se ha creado correctamente (ok: 1)
```
<img src="images\02_create_collection.png">

# Listar las bases de datos, sino tiene colecciones no se Lista
```mongodb
show databases;  // Muestra una lista de todas las bases de datos disponibles en el servidor MongoDB 
```
<img src="images\03_show_databases.png">

# Eliminar una coleccion
```mongodb
db.test_collection.drop();  // Elimina la colección llamada 'test_collection' de la base de datos actual
```
<img src="images\04_drop_collection.png">

# Eliminar una base de datos
```mongodb
db.dropDatabase();  // Elimina la base de datos actual (test_db) junto con todas sus colecciones
```
<img src="images\05_drop_database.png">

# Seleccionar una base de datos que ya existe, sino existe la crea vacia
```mongodb
use RetailManagementDB;  // Cambia el contexto de la base de datos a 'RetailManagementDB'
```
<img src="images\06_change_database.png">

# Listar las colecciones de la base de datos Seleccionada
```mongodb
show collections;  // Muestra una lista de todas las colecciones disponibles en la base de datos actual (RetailManagementDB)
```
<img src="images\07_show_collections.png">

# Crear un Indice generico en la colección
```mongodb
db.Customers.createIndex({
    customer_id: 1  // Crea un índice ascendente en el campo customer_id en la colección Customers
});
```
<img src="images\08_create_generic_index.png">


# Crear un Indice con nombre personalizado en la colección
```mongodb
db.Orders.createIndex(
    { customer_id: 1 },          // Crea un índice ascendente en el campo customer_id en la colección Orders
    { name: "idx_customer_id" }  // Nombre personalizado asignado al índice: idx_customer_id
);
```
<img src="images\09_create_custom_name_index.png">

# Crear un multiples indices en la colección
```mongodb
db.Payments.createIndexes(
   [
     {
       "payment_id": 1
     },
     {
       "order_id": 1
     },
     {
       "payment_date": -1
     },
     {
       "payment_method": 1
     }
   ]
 );
```
<img src="images\10_create_multiple_indexes.png">

# Consultar Indices  en la colección
```mongodb
db.Customers.getIndexes();
```
<img src="images\11_check_all_indexes.png">

# Elimina todos los indices presentes en la colección excepto _id
```mongodb
db.Payments.dropIndexes(); // Elimina todos los índices excepto _id
```
<img src="images\12_drop_all_indexes.png">

# Eliminar Indices
```mongodb
db.Orders.dropIndex('order_id_1');  // Elimina el índice llamado 'order_id_1' de la colección Orders
```
<img src="images\13_drop_one_index.png">

# Insertar 1 documento de una coleccion
```mongodb
db.Customers.insertOne({  // Inserta un nuevo documento en la colección Customers
    customer_id: 1235,      // Campo que representa el ID del cliente
    name: "Nathalie Cardona", // Campo que representa el nombre del cliente
    age: 30                 // Campo que representa la edad del cliente
});
```
<img src="images\14_insert_one.png">

# Insertar multiples documentos de una coleccion, en un solo query
```mongodb
db.Customers.insertMany([  // Inserta múltiples documentos en la colección Customers
    {
        customer_id: 1236,    // Campo que representa el ID del cliente
        name: "Carlos Perez",  // Campo que representa el nombre del cliente
        age: 35,               // Campo que representa la edad del cliente
        salary: 2500,          // Este campo está definido
        phone: null,           // Este campo está definido como null
        address: "123 Calle Falsa"  // Campo que representa la dirección del cliente
    },
    {
        customer_id: 1237,    // Campo que representa el ID del cliente
        name: "Ana Torres",    // Campo que representa el nombre del cliente
        age: 28,               // Campo que representa la edad del cliente
        // salary y phone no están definidos aquí
        address: "456 Avenida Real"  // Campo que representa la dirección del cliente
    },
    {
        customer_id: 1238,    // Campo que representa el ID del cliente
        name: "Luis Gonzalez",  // Campo que representa el nombre del cliente
        age: 45,               // Campo que representa la edad del cliente
        salary: 3200,          // Este campo está definido
        // phone y address no están definidos aquí
    },
    {
        customer_id: 1239,    // Campo que representa el ID del cliente
        name: "Laura Martinez", // Campo que representa el nombre del cliente
        age: 50,               // Campo que representa la edad del cliente
        salary: null,          // Este campo está definido como null
        phone: null,           // Este campo está definido como null
        address: "789 Plaza Central"  // Campo que representa la dirección del cliente
    }
]);
```
<img src="images\15_insert_many.png">

# Eliminar 1 documento de una coleccion, basado en una condicion
```mongodb
db.Customers.deleteOne(  // Elimina un documento de la colección Customers que coincide con el criterio especificado
    { customer_id: 0 }     // Criterio de búsqueda: busca un documento donde customer_id sea igual a 0
);
```
<img src="images\16_delete_one.png">

# Eliminar todos documentos de una coleccion, que cumplan la condicion
```mongodb
db.Customers.deleteMany(  // Elimina múltiples documentos de la colección Customers que coinciden con el criterio especificado
    { customer_id: { $gt: 10 }}  // Criterio de búsqueda: busca documentos donde customer_id sea mayor que 10
);
```
<img src="images\17_delete_many.png">

# Actualizar 1 documento de una coleccion, basado en una condicion
```mongodb
db.Customers.updateOne(  // Actualiza un único documento en la colección Customers que coincide con el criterio especificado
    { customer_id: 1 },    // Criterio de búsqueda: busca un documento donde customer_id sea igual a 1
    { $set: { salary: 2222 } }  // Actualiza el campo salary, estableciendo su valor en 2222
);
```
<img src="images\18_update_one.png">

# Actualizar todos documentos de una coleccion, que cumplan la condicion
```mongodb
db.Customers.updateMany(  // Actualiza múltiples documentos en la colección Customers que coinciden con el criterio especificado
    { salary: { $lt: 3000 } }, // Criterio de búsqueda: busca documentos donde el salario sea menor a 3000
    { $inc: { salary: 500 } }  // Incrementa el campo salary en 500 para todos los documentos que coinciden
);
```
<img src="images\19_update_many_1.png">

# Actualizar todos documentos de una coleccion, que cumplan las condiciones
```mongodb
db.Customers.updateMany(  // Actualiza múltiples documentos en la colección Customers que coinciden con el criterio especificado
    { salary: { $lt: 4000 }, age: { $gt: 40 } },  // Criterio de búsqueda: busca documentos donde el salario sea menor a 4000 y la edad mayor a 40
    { $mul: { salary: 1.5 } }                     // Multiplica el campo salary por 1.5 para todos los documentos que coinciden
);
```
<img src="images\20_update_many_2.png">

# UPSERT Actualizar o insertar un documentos de una coleccion, que cumplan las condiciones
```mongodb
db.Customers.updateOne(  // Actualiza un único documento en la colección Customers que coincide con el criterio especificado
    { customer_id: 1234 },  // Criterio de búsqueda: busca un documento donde customer_id sea igual a 1234
    { 
        $set: {               // Operación de actualización: establece los siguientes campos
            name: "Jorge Cardona",  // Campo que representa el nombre del cliente
            age: 31,               // Campo que representa la edad del cliente
            nationality: "Unknown",  // Campo que representa la nacionalidad del cliente
            current_continent: "Oceania"  // Campo que representa el continente donde reside actualmente el cliente
        } 
    },  
    { upsert: true }         // Opción upsert: si no encuentra coincidencias, inserta un nuevo documento
);
```
<img src="images\21_upsert_one.png">

# UPSERT Actualizar o insertar un documentos de una coleccion, que cumplan las condiciones
```mongodb
db.Customers.updateMany(  // Actualiza múltiples documentos en la colección Customers que coinciden con el criterio especificado
    { nationality: "Unknown" },       // Criterio de búsqueda: busca documentos donde la nacionalidad sea "Unknown"
    { $set: { nationality: "Pereira" } }, // Actualiza el campo nationality, estableciendo su valor en "Pereira"
    { upsert: true }                  // Opción upsert: si no encuentra coincidencias, inserta un nuevo documento
);
```
<img src="images\22_upsert_many.png">


# recuperar el primer documento de la coleccion
```mongodb
db.Customers.findOne(); // Utiliza el método findOne() para obtener el primer documento de la colección Customers.
```
<img src="images\23_find_one.png">


# recuperar todos los documentos de la coleccion
```mongodb
db.Customers.find(); // Usa el método find() para obtener todos los documentos de la colección Customers.
```
<img src="images\24_find_all.png">

# Recuperar los primeros 2 documentos de la colección
# Utiliza el método find() para obtener todos los documentos de la colección Customers,
# y luego aplica limit(2) para devolver solo los primeros dos documentos.
```mongodb
db.Customers.find().limit(2);
```
<img src="images\25_find_limit.png">

# Contar cuántos documentos hay en la colección Customers
# Utiliza el método countDocuments() para devolver el número total de documentos en la colección.
```mongodb
db.Customers.countDocuments();
```
<img src="images\26_count.png">

# Contar cuántos documentos hay en la colección Customers
# Utiliza el método countDocuments() para devolver el número total de documentos en la colección.
```mongodb
db.Customers.countDocuments();
```
<img src="images\26_count.png">

# Recuperar todos los documentos pero mostrando solo los primeros tres campos (_id, customer_id, name)
# Utiliza el método find() y la proyección para incluir solo los campos deseados.
```mongodb
db.Customers.find({}, { _id: 1, customer_id: 1, name: 1 }).limit(4)
```
<img src="images\28_filter_equals.png">

# Recuperar todos los documentos menores que la condicion
```mongodb
db.Customers.find(
    {
        'customer_id': { $lt: 2 } // Filtro de búsqueda: Busca documentos donde el campo 'customer_id' sea menor que 2
    }
);
```
<img src="images\29_filter_lower_than.png">


# Recuperar todos los documentos menores o iguales que la condicion
```mongodb
db.Customers.find(
    {
        'customer_id': { $lte: 2 } // Filtro de búsqueda: Busca documentos donde el campo 'customer_id' sea menor o igual a 2
    }
);
```
<img src="images\30_filter_lower_or_equals_than.png">


# Recuperar todos los documentos mayores que la condicion
```mongodb
db.Customers.find(
    {
        'customer_id': { $gt: 10 } // Filtro de búsqueda: Busca documentos donde el campo 'customer_id' sea mayor que 10
    }
);
```
<img src="images\31_filter_greater_than.png">


# Recuperar todos los documentos que cumplan la condicion del or
```mongodb
db.Customers.find(
    {
        '$or': [ // Operador lógico: Busca documentos que cumplen al menos una de las condiciones
            { 'customer_id': { $gt: 10 } }, // Condición 1: 'customer_id' es mayor que 10
            { 'customer_id': { $lt: 2 } }   // Condición 2: 'customer_id' es menor que 2
        ]
    }
);
```
<img src="images\32_filter_or_condition.png">


# Recuperar todos los documentos que cumplan la condicion del and
```mongodb
db.Customers.find(
    {
        '$and': [ // Operador lógico: Busca documentos que cumplen ambas condiciones
            { 'customer_id': { $gt: 1 } }, // Condición 1: 'customer_id' es mayor que 1
            { 'salary': { $gt: 9000 } }     // Condición 2: 'salary' es mayor que 9000
        ]
    }
);
```
<img src="images\33_filter_and_condition.png">

# Recuperar todos los documentos que cumplan la condicion del and y el or
```mongodb
db.Customers.find(
    {
        '$or': [ // Operador lógico: Busca documentos que cumplen al menos una de las condiciones
            { // Primera condición del $or
                '$and': [ // Operador lógico: Ambas condiciones dentro de este grupo deben cumplirse
                    { 'customer_id': { $gt: 10 } }, // 'customer_id' debe ser mayor que 10
                    { 'salary': { $gt: 3000 } }     // 'salary' debe ser mayor que 3000
                ]
            },
            { // Segunda condición del $or
                'age': { $lt: 30 } // 'age' debe ser menor que 30
            }
        ]
    }
);
```
<img src="images\34_filter_and_or_condition.png">


# Recuperar todos los documentos que cumplan la condicion del and y ordenarlo de manera descendete
```mongodb
db.Customers.find(
    {
        // Usamos el operador lógico '$and' para cumplir con ambas condiciones
        '$and': [ 
            { 
                'customer_id': { $gt: 1 } // Condición 1: Selecciona documentos donde 'customer_id' es mayor que 1
            },  
            { 
                'salary': { $gt: 9000 }   // Condición 2: Selecciona documentos donde 'salary' es mayor que 9000
            }     
        ]
    }
)
.sort({ 
    'salary': -1  // Ordena los resultados por el campo 'salary' en orden descendente (de mayor a menor)
});
```
<img src="images\35_filter_and_order_descending.png">


# Agrupacion, agregado, Recuperar todos los documentos agrupados y ordenados segun la condicion
```mongodb
db.Customers.aggregate([
    {
        $group: {  // Inicia la etapa de agrupación
            _id: "$current_continent",  // Agrupa los documentos por el campo 'current_continent'
            total_customers: { $sum: 1 },  // Cuenta el número de clientes en cada continente
            total_salary: { $sum: "$salary" },  // Suma los salarios de los clientes en cada continente
            avg_age: { $avg: "$age" },  // Calcula la edad promedio de los clientes en cada continente
            min_age: { $min: "$age" },  // Encuentra la edad mínima de los clientes en cada continente
            max_age: { $max: "$age" },  // Encuentra la edad máxima de los clientes en cada continente
            std_dev_age: { $stdDevPop: "$age" },  // Calcula la desviación estándar poblacional de la edad
            high_salary_count: { $sum: { $cond: [{ $gt: ["$salary", 5000] }, 1, 0] } },  // Cuenta los clientes con salario mayor a 5000
            unique_nationalities: { $addToSet: "$nationality" }  // Crea un array de nacionalidades únicas de los clientes en cada continente
        }
    },
    {
        $sort: {  // Inicia la etapa de ordenación
            avg_age: 1,  // Ordena los resultados por 'avg_age' en orden ascendente
            total_salary: -1,  // Ordena los resultados por 'total_salary' en orden descendente
            total_customers: -1  // Ordena los resultados por 'total_customers' en orden descendente
        }
    }
]);
```
<img src="images\36_grouped_and_sorted.png">


# Agregación de Clientes con Órdenes: Inner Join V1
```mongodb
db.Customers.aggregate([  // Inicia una operación de agregación en la colección Customers
    {
        // Realiza el join entre la colección Customers y Orders
        $lookup: {
            from: "Orders",              // Especifica la colección con la que estamos haciendo el join (Orders)
            localField: "customer_id",   // Campo en Customers que será usado para el match
            foreignField: "customer_id",  // Campo en Orders que será comparado con el campo en Customers
            as: "orders_inner_join_v1"    // El resultado del join se guardará en este nuevo campo
        }
    },
    {
        // Filtra los resultados del join
        $match: {
            "orders_inner_join_v1": { $ne: [] } // Incluye solo los documentos que tienen órdenes, es decir, que no tienen el array vacío
        }
    }
]);
```

# inner join v1, ver el plan de ejecucion
```mongodb
db.Customers.aggregate([  // Inicia una operación de agregación en la colección Customers
    {
        // Realiza el join entre la colección Customers y Orders
        $lookup: {
            from: "Orders",              // Especifica la colección con la que estamos haciendo el join (Orders)
            localField: "customer_id",   // Campo en Customers que será usado para el match
            foreignField: "customer_id",  // Campo en Orders que será comparado con el campo en Customers
            as: "orders_inner_join_v1"    // El resultado del join se guardará en este nuevo campo
        }
    },
    {
        // Filtra los resultados del join
        $match: {
            "orders_inner_join_v1": { $ne: [] } // Incluye solo los documentos que tienen órdenes, es decir, que no tienen el array vacío
        }
    }
]).explain("executionStats");  // Ejecuta la operación y devuelve estadísticas de ejecución sobre el pipeline de agregación
```

# inner join v1, documento anidado conteos antes y despues del join, ademas de todos los documentos
```mongodb
db.Customers.aggregate([  // Inicia una operación de agregación en la colección Customers
    {
        // Realiza el join entre Customers y Orders
        $lookup: {
            from: "Orders",                // Colección Orders con la cual estamos haciendo el join
            localField: "customer_id",     // Campo en Customers que se usará para hacer el match
            foreignField: "customer_id",    // Campo en Orders con el que se comparará
            as: "orders_inner_join_v3"      // Nombre del campo que contendrá las órdenes relacionadas
        }
    },
    {
        $facet: {  // Permite realizar múltiples operaciones en paralelo sobre el resultado del pipeline
            // Cuenta el número total de documentos después del lookup (antes de aplicar cualquier filtro)
            total_documents: [
                { $count: "count" } // Cuenta cuántos documentos hay en total en el pipeline
            ],
            // Cuenta solo los documentos que tienen órdenes (join no vacío)
            total_documents_with_orders: [
                { $match: { "orders_inner_join_v3": { $ne: [] } } }, // Filtra para obtener solo los documentos con órdenes
                { $count: "count" } // Cuenta cuántos de esos documentos tienen órdenes
            ],
            // Retorna solo los documentos que tienen órdenes (join válido)
            all_documents_with_orders: [ 
                { $match: { "orders_inner_join_v3": { $ne: [] } } }, // Filtra para obtener solo los documentos con órdenes 
            ]
        }
    }
]);
```

# INNER JOIN MUESTRA SOLO LOS DOCUMENTOS QUE TIENEN ANDIDADOS ENTRE 2 Y 3 DOCUMENTOS
```mongodb
db.Customers.aggregate([  // Inicia una operación de agregación en la colección Customers
    {
        // Realiza un join entre la colección Customers y Orders
        $lookup: {
            from: "Orders",                   // Colección a la que se está uniendo
            localField: "customer_id",        // Campo en Customers que se usa para el join
            foreignField: "customer_id",      // Campo en Orders que se usa para el join
            as: "orders_inner_join_v1"        // Nombre del nuevo campo que contendrá las órdenes
        }
    },
    {
        // Filtra los resultados para incluir solo aquellos que cumplen ciertas condiciones
        $match: {
            // Asegura que el tamaño de orders_inner_join_v1 sea mayor o igual a 2 y menor o igual a 3
            $expr: { 
                $and: [
                    { $gte: [{ $size: "$orders_inner_join_v1" }, 2] }, // Al menos 2 documentos
                    { $lte: [{ $size: "$orders_inner_join_v1" }, 3] }  // Máximo 3 documentos
                ]
            }
        }
    },
    {
        $count: "total_documents" // Cuenta el número total de documentos que cumplen con las condiciones
    }
]);
```

# INNER JOIN MUESTRA EL TOTAL DE DOCUMENTOS QUE CUMPLEN CON LA CONSULTA
```mongodb
db.Customers.aggregate([  // Inicia una operación de agregación en la colección Customers
    {
        $lookup: {  // Realiza un join entre la colección Customers y Orders
            from: "Orders",                  // Colección a la que se está uniendo
            localField: "customer_id",       // Campo en Customers que se usa para el join
            foreignField: "customer_id",     // Campo en Orders que se usa para el join
            as: "orders_inner_join_v1"       // Nombre del nuevo campo que contendrá las órdenes
        }
    },
    {
        $match: {  // Filtra los documentos que cumplen con las condiciones
            "orders_inner_join_v1": { $ne: [] } // Filtra los documentos que tienen orders_inner_join no vacío
        }
    },
    {
        $count: "total_documents" // Cuenta el número total de documentos que cumplen con las condiciones
    }
]);
```

# INNER JOIN CON CONDICION
```mongodb
db.Customers.aggregate([  // Inicia una operación de agregación en la colección Customers
    {
        $lookup: {  // Realiza un join entre la colección Customers y Orders
            from: "Orders",                  // Colección a la que se está uniendo
            localField: "customer_id",       // Campo en Customers que se usa para el join
            foreignField: "customer_id",     // Campo en Orders que se usa para el join
            as: "orders_inner_join_condition" // Nombre del nuevo campo que contendrá las órdenes
        }
    },
    {
        $match: {  // Filtra los documentos que cumplen con las condiciones
            "orders_inner_join_condition": { $ne: [] }, // Filtra los documentos que tienen orders_inner_join no vacío
            "customer_id": 3 // Agrega la condición para customer_id
        }
    }
]);
```

# INNER Join, v2 documento Relacionado por documento
```mongodb
db.Customers.aggregate([  // Inicia una operación de agregación en la colección Customers
    {
        $lookup: {  // Realiza un join entre la colección Customers y Orders
            from: "Orders",                  // Colección a la que se está uniendo
            localField: "customer_id",       // Campo en Customers que se usa para el join
            foreignField: "customer_id",     // Campo en Orders que se usa para el join
            as: "orders_inner_join_v2"       // Nombre del nuevo campo que contendrá las órdenes
        }
    },
    {
        $unwind: "$orders_inner_join_v2" // Descompone el array de órdenes en documentos individuales
    },
    {
        $match: {  // Filtra los documentos que cumplen con las condiciones
            "orders_inner_join_v2": { $ne: [] } // Asegura que solo se incluyan los documentos con órdenes
        }
    }
]);
```

# INNER JOIN MUESTRA EL TOTAL DE DOCUMENTOS QUE CUMPLEN CON LA CONSULTA
```mongodb
db.Customers.aggregate([  // Inicia una operación de agregación en la colección Customers
    {
        $lookup: {  // Realiza un join entre la colección Customers y Orders
            from: "Orders",                  // Colección a la que se está uniendo
            localField: "customer_id",       // Campo en Customers que se usa para el join
            foreignField: "customer_id",     // Campo en Orders que se usa para el join
            as: "orders_inner_join_v2"       // Nombre del nuevo campo que contendrá las órdenes
        }
    },
    {
        $unwind: "$orders_inner_join_v2" // Descompone el array de órdenes en documentos individuales
    },
    {
        $match: {  // Filtra los documentos que cumplen con las condiciones
            "orders_inner_join_v2": { $ne: [] } // Asegura que solo se incluyan los documentos con órdenes
        }
    },
    {
        $count: "total_documents" // Cuenta el número total de documentos que cumplen con las condiciones
    }
]);
```


# INNER Join, v3 documento Relacionado por documento, pero con los campos combinados en un solo documento
```mongodb
db.Customers.aggregate([  // Inicia una operación de agregación en la colección Customers
    {
        $lookup: {  // Realiza un join entre la colección Customers y Orders
            from: "Orders",                  // Colección a la que se está uniendo
            localField: "customer_id",       // Campo en Customers que se usa para el join
            foreignField: "customer_id",     // Campo en Orders que se usa para el join
            as: "orders_inner_join_v3"       // Nombre del nuevo campo que contendrá las órdenes
        }
    },
    {
        $unwind: "$orders_inner_join_v3" // Descompone el array de órdenes en documentos individuales
    },
    {
        $match: {  // Filtra los documentos que cumplen con las condiciones
            "orders_inner_join_v3": { $ne: [] } // Asegura que solo se incluyan los documentos con órdenes
        }
    },
    {
        $replaceRoot: {  // Reemplaza la raíz del documento
            newRoot: { $mergeObjects: ["$$ROOT", "$orders_inner_join_v3"] } // Combina los campos de Customers y Orders
        }
    },
    {
        $project: {  // Proyecta los campos que se desean incluir o excluir
            orders_inner_join_v3: 0 // Opcional: Si no deseas mostrar el array de órdenes original
        }
    }
]);
```

# LEFT JOIN
```mongodb
db.Customers.aggregate([  // Inicia una operación de agregación en la colección Customers
    {
        $lookup: {  // Realiza un join entre la colección Customers y Orders
            from: "Orders",                  // Colección a la que se está uniendo
            localField: "customer_id",       // Campo en Customers que se usa para el join
            foreignField: "customer_id",     // Campo en Orders que se usa para el join
            as: "orders_left_join"           // Nombre del nuevo campo que contendrá las órdenes
        }
    }
]);
```

# LEFT JOIN, solo los primeros 10 documentos, ordenando por los no vacios primero
```mongodb
db.Customers.aggregate([  // Inicia una operación de agregación en la colección Customers
    {
        $lookup: {  // Realiza un join entre la colección Customers y Orders
            from: "Orders",                  // Colección a la que se está uniendo
            localField: "customer_id",       // Campo en Customers que se usa para el join
            foreignField: "customer_id",     // Campo en Orders que se usa para el join
            as: "orders_left_join"           // Nombre del nuevo campo que contendrá las órdenes
        }
    },
    {
        $sort: {  // Ordena los documentos en la salida
            "orders_left_join": -1 // Ordena en orden descendente (de mayor a menor) por el campo orders_left_join
        }
    },
    {
        $limit: 10 // Limita los resultados a los primeros 10 documentos
    }
]);
```

# ANTI LEFT JOIN
```mongodb
db.Customers.aggregate([  // Inicia una operación de agregación en la colección Customers
    {
        $lookup: {  // Realiza un join entre la colección Customers y Orders
            from: "Orders",                      // La colección con la que estás haciendo el join
            localField: "customer_id",           // Campo en Customers que se usará para el join
            foreignField: "customer_id",         // Campo en Orders que se usará para el join
            as: "orders_anti_left_join"               // El nombre del campo nuevo donde se guardarán las órdenes
        }
    },
    {
        $match: {  // Filtra los resultados de la agregación
            "orders_anti_left_join": { $eq: [] }     // Incluye solo los documentos donde el arreglo de órdenes está vacío
        }
    }
]);
```

# RIGHT JOIN, se invierten las colecciones del left join
```mongodb
db.Orders.aggregate([  // Inicia una operación de agregación en la colección Orders
    {
        $lookup: {  // Realiza un join entre la colección Orders y Customers
            from: "Customers",                // Colección a la que se está uniendo
            localField: "customer_id",        // Campo en Orders que se usa para el join
            foreignField: "customer_id",      // Campo en Customers que se usa para el join
            as: "customers_right_join"        // Nombre del nuevo campo que contendrá los clientes
        }
    },
    {
        $match: {  // Filtra los resultados de la agregación
            "customers_right_join": { $ne: [] }  // Incluye solo los documentos donde el arreglo de clientes no está vacío
        }
    }
]);
```

# ANTI RIGHT JOIN
```mongodb
db.Orders.aggregate([  // Inicia una operación de agregación en la colección Orders
    {
        $lookup: {  // Realiza un join entre la colección Orders y Customers
            from: "Customers",                  // La colección con la que estás haciendo el join
            localField: "customer_id",          // Campo en Orders que se usará para el join
            foreignField: "customer_id",        // Campo en Customers que se usará para el join
            as: "orders_anti_right_join"        // El nombre del nuevo campo donde se guardarán las órdenes
        }
    },
    {
        $match: {  // Filtra los resultados de la agregación
            "orders_anti_right_join": { $eq: [] }  // Incluye solo los documentos donde el arreglo de órdenes está vacío
        }
    }
]);
```