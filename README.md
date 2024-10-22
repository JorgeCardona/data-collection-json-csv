# data-collection-json-csv-sql
data-collection-json-csv-sql is a repository dedicated to storing a variety of datasets in both JSON, SQL and CSV formats. This collection includes data from different domains and can be used for data analysis, machine learning projects, or educational purposes.

# Crear bases de datos
```mongodb
> use test_db  // Cambia el contexto de la base de datos a 'test_db'
< switched to db test_db  // Mensaje de confirmación que indica que se ha cambiado a la base de datos 'test_db'
```

# Crear una coleccion
```mongodb
> db.createCollection('test_collection');  // Crea una nueva colección llamada 'test_collection' en la base de datos actual
< { ok: 1 }  // Mensaje de confirmación que indica que la colección se ha creado correctamente (ok: 1)
```

# Listar las bases de datos, sino tiene colecciones no se Lista
```mongodb
> show databases  // Muestra una lista de todas las bases de datos disponibles en el servidor MongoDB
RetailManagementDB  240.00 KiB  // Nombre de la base de datos y su tamaño
admin               100.00 KiB  // Nombre de la base de datos y su tamaño
config              108.00 KiB  // Nombre de la base de datos y su tamaño
local                80.00 KiB  // Nombre de la base de datos y su tamaño
sample_analytics      9.48 MiB  // Nombre de la base de datos y su tamaño
spark                 1.04 MiB  // Nombre de la base de datos y su tamaño
test_db               8.00 KiB  // Nombre de la base de datos y su tamaño
```

# Eliminar una coleccion
```mongodb
> db.test_collection.drop();  // Elimina la colección llamada 'test_collection' de la base de datos actual
< true  // Mensaje de confirmación que indica que la colección se ha eliminado correctamente (true)
```

# Eliminar una base de datos
```mongodb
> db.dropDatabase();  // Elimina la base de datos actual (test_db) junto con todas sus colecciones
< { ok: 1, dropped: 'test_db' }  // Mensaje de confirmación que indica que la base de datos 'test_db' se ha eliminado correctamente (ok: 1)
```

# Seleccionar una base de datos que ya existe, sino existe la crea vacia
```mongodb
> use RetailManagementDB  // Cambia el contexto de la base de datos a 'RetailManagementDB'
< switched to db RetailManagementDB  // Mensaje de confirmación que indica que se ha cambiado a la base de datos 'RetailManagementDB'
```

# Listar las colecciones de la base de datos Seleccionada
```mongodb
> show collections  // Muestra una lista de todas las colecciones disponibles en la base de datos actual (RetailManagementDB)
Customers           // Nombre de la colección 'Customers'
new_collection      // Nombre de la colección 'new_collection'
Orders              // Nombre de la colección 'Orders'
Payments            // Nombre de la colección 'Payments'
```

# Crear un Indice en la colección y un indice con nombre personalizado
```mongodb
> db.Customers.createIndex({
    customer_id: 1  // Crea un índice ascendente en el campo customer_id en la colección Customers
});

customer_id_1  // Nombre automático del índice basado en el campo customer_id

> db.Orders.createIndex(
    { customer_id: 1 },          // Crea un índice ascendente en el campo customer_id en la colección Orders
    { name: "idx_customer_id" }  // Nombre personalizado asignado al índice: idx_customer_id
);

idx_customer_id  // Nombre personalizado del índice creado
```

# Crear un multiples indices en la colección
```mongodb
> db.Payments.createIndexes([
    { key: { order_id: 1 }, name: "idx_order_id" },         // Crea un índice ascendente para el campo order_id
    { key: { customer_id: 1 }, name: "idx_customer_id" },   // Crea un índice ascendente para el campo customer_id
    { key: { order_date: -1 }, name: "idx_order_date_desc" } // Crea un índice descendente para el campo order_date
]);
```

# Consultar Indices  en la colección
```mongodb
> db.Customers.getIndexes();
[
  { v: 2, key: { _id: 1 }, name: '_id_' },                // Índice predeterminado en el campo _id, creado automáticamente por MongoDB
  { v: 2, key: { customer_id: 1 }, name: 'customer_id_1' } // Índice ascendente en el campo customer_id
]

> db.Orders.getIndexes();
[
  { v: 2, key: { _id: 1 }, name: '_id_' },               // Índice predeterminado en el campo _id, creado automáticamente por MongoDB
  { v: 2, key: { customer_id: 1 }, name: 'idx_customer_id' } // Índice ascendente en el campo customer_id, con un nombre personalizado
]
```

# Eliminar Indices
```mongodb
> db.Orders.dropIndex('order_id_1');  // Elimina el índice llamado 'order_id_1' de la colección Orders
{ nIndexesWas: 2, ok: 1 }  // Había 2 índices antes de eliminar, operación exitosa (ok: 1)

> db.Orders.getIndexes();  // Obtiene todos los índices de la colección Orders
[
  { v: 2, key: { _id: 1 }, name: '_id_' }  // Índice predeterminado en el campo _id, creado automáticamente por MongoDB
]
```


# Insertar 1 documento de una coleccion
```mongodb
> db.Customers.insertOne({  // Inserta un nuevo documento en la colección Customers
    customer_id: 1235,      // Campo que representa el ID del cliente
    name: "Maria Lopez",    // Campo que representa el nombre del cliente
    age: 30                 // Campo que representa la edad del cliente
});

< { 
  acknowledged: true,      // Indica que la operación de inserción fue reconocida
  insertedId: ObjectId('6717017f928cf000615c3873')  // ID del documento insertado en la colección
}
```

# Insertar multiples documentos de una coleccion, en un solo query
```mongodb
> db.Customers.insertMany([  // Inserta múltiples documentos en la colección Customers
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

< { 
  acknowledged: true,        // Indica que la operación de inserción fue reconocida
  insertedIds: {            // Objeto que contiene los IDs de los documentos insertados
    '0': ObjectId('67170291928cf000615c3875'),  // ID del primer documento insertado
    '1': ObjectId('67170291928cf000615c3876'),  // ID del segundo documento insertado
    '2': ObjectId('67170291928cf000615c3877'),  // ID del tercer documento insertado
    '3': ObjectId('67170291928cf000615c3878')   // ID del cuarto documento insertado
  }
}
```

# Eliminar 1 documento de una coleccion, basado en una condicion
```mongodb
> db.Customers.deleteOne(  // Elimina un documento de la colección Customers que coincide con el criterio especificado
    { customer_id: 0 }     // Criterio de búsqueda: busca un documento donde customer_id sea igual a 0
);

< { 
  acknowledged: true,      // Indica que la operación de eliminación fue reconocida
  deletedCount: 1         // Número de documentos eliminados, en este caso, 1
}
```

# Eliminar todos documentos de una coleccion, que cumplan la condicion
```mongodb
> db.Customers.deleteMany(  // Elimina múltiples documentos de la colección Customers que coinciden con el criterio especificado
    { customer_id: { $gt: 10 }}  // Criterio de búsqueda: busca documentos donde customer_id sea mayor que 10
);

< { 
  acknowledged: true,      // Indica que la operación de eliminación fue reconocida
  deletedCount: 89        // Número de documentos eliminados, en este caso, 89
}
```

# Actualizar 1 documento de una coleccion, basado en una condicion
```mongodb
> db.Customers.updateOne(  // Actualiza un único documento en la colección Customers que coincide con el criterio especificado
    { customer_id: 1 },    // Criterio de búsqueda: busca un documento donde customer_id sea igual a 1
    { $set: { salary: 2222 } }  // Actualiza el campo salary, estableciendo su valor en 2222
);

< { 
  acknowledged: true,      // Indica que la operación de actualización fue reconocida
  insertedId: null,       // No se insertó un nuevo documento (null)
  matchedCount: 1,        // Número de documentos que coincidieron con el criterio de búsqueda, en este caso, 1
  modifiedCount: 1,       // Número de documentos que fueron modificados, en este caso, 1
  upsertedCount: 0        // Número de documentos insertados (upsert) en caso de que no se encontrara ninguno, en este caso, 0
}
```

# Actualizar todos documentos de una coleccion, que cumplan la condicion
```mongodb
> db.Customers.updateMany(  // Actualiza múltiples documentos en la colección Customers que coinciden con el criterio especificado
    { salary: { $lt: 3000 } }, // Criterio de búsqueda: busca documentos donde el salario sea menor a 3000
    { $inc: { salary: 500 } }  // Incrementa el campo salary en 500 para todos los documentos que coinciden
);

< { 
  acknowledged: true,      // Indica que la operación de actualización fue reconocida
  insertedId: null,       // No se insertó un nuevo documento (null)
  matchedCount: 4,        // Número de documentos que coincidieron con el criterio de búsqueda, en este caso, 4
  modifiedCount: 4,       // Número de documentos que fueron modificados, en este caso, 4
  upsertedCount: 0        // Número de documentos insertados (upsert) en caso de que no se encontrara ninguno, en este caso, 0
}
```

# Actualizar todos documentos de una coleccion, que cumplan las condiciones
```mongodb
> db.Customers.updateMany(  // Actualiza múltiples documentos en la colección Customers que coinciden con el criterio especificado
    { salary: { $lt: 4000 }, age: { $gt: 40 } },  // Criterio de búsqueda: busca documentos donde el salario sea menor a 4000 y la edad mayor a 40
    { $mul: { salary: 1.5 } }                     // Multiplica el campo salary por 1.5 para todos los documentos que coinciden
);

< { 
  acknowledged: true,      // Indica que la operación de actualización fue reconocida
  insertedId: null,       // No se insertó un nuevo documento (null)
  matchedCount: 3,        // Número de documentos que coincidieron con el criterio de búsqueda, en este caso, 3
  modifiedCount: 3,       // Número de documentos que fueron modificados, en este caso, 3
  upsertedCount: 0        // Número de documentos insertados (upsert) en caso de que no se encontrara ninguno, en este caso, 0
}
```

# UPSERT Actualizar o insertar un documentos de una coleccion, que cumplan las condiciones
```mongodb
> db.Customers.updateOne(  // Actualiza un único documento en la colección Customers que coincide con el criterio especificado
    { customer_id: 1234 },  // Criterio de búsqueda: busca un documento donde customer_id sea igual a 1234
    { 
        $set: {               // Operación de actualización: establece los siguientes campos
            name: "Jorge Cardona",  // Campo que representa el nombre del cliente
            age: 31,               // Campo que representa la edad del cliente
            nationality: "Unknown"  // Campo que representa la nacionalidad del cliente
        } 
    },  
    { upsert: true }         // Opción upsert: si no encuentra coincidencias, inserta un nuevo documento
);

< { 
  acknowledged: true,      // Indica que la operación de actualización fue reconocida
  insertedId: ObjectId('6716fe2dc8f95dbf82f9a593'),  // ID del documento insertado (nuevo documento)
  matchedCount: 0,        // Número de documentos que coincidieron con el criterio de búsqueda, en este caso, 0
  modifiedCount: 0,       // Número de documentos que fueron modificados, en este caso, 0
  upsertedCount: 1        // Número de documentos insertados (upsert), en este caso, 1
}
```

# UPSERT Actualizar o insertar un documentos de una coleccion, que cumplan las condiciones
```mongodb
> db.Customers.updateMany(  // Actualiza múltiples documentos en la colección Customers que coinciden con el criterio especificado
    { nationality: "Unknown" },       // Criterio de búsqueda: busca documentos donde la nacionalidad sea "Unknown"
    { $set: { nationality: "Pereira" } }, // Actualiza el campo nationality, estableciendo su valor en "Pereira"
    { upsert: true }                  // Opción upsert: si no encuentra coincidencias, inserta un nuevo documento
);

< { 
  acknowledged: true,      // Indica que la operación de actualización fue reconocida
  insertedId: null,       // No se insertó un nuevo documento (null)
  matchedCount: 1,        // Número de documentos que coincidieron con el criterio de búsqueda, en este caso, 1
  modifiedCount: 1,       // Número de documentos que fueron modificados, en este caso, 1
  upsertedCount: 0        // Número de documentos insertados (upsert), en este caso, 0
}
```

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
            "customer_id": 34 // Agrega la condición para customer_id
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

# ANTI LEFT JOIN
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
