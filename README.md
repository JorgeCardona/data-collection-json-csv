# data-collection-json-csv-sql
data-collection-json-csv-sql is a repository dedicated to storing a variety of datasets in both JSON, SQL and CSV formats. This collection includes data from different domains and can be used for data analysis, machine learning projects, or educational purposes.

# MongoDB Documentation
# Crear bases de datos
```mongodb
> use test_db
< switched to db test_db
```

# Crear una coleccion
```mongodb
> db.createCollection('test_collection');
< { ok: 1 }
```

# Listar las bases de datos, sino tiene colecciones no se Lista
```mongodb
> show databases
RetailManagementDB  240.00 KiB
admin               100.00 KiB
config              108.00 KiB
local                80.00 KiB
sample_analytics      9.48 MiB
spark                 1.04 MiB
test_db               8.00 KiB
```

# Eliminar una coleccion
```mongodb
> db.test_collection.drop();
< true
```

# Eliminar una base de datos
```mongodb
> db.dropDatabase();
< { ok: 1, dropped: 'test_db' }
```

# Seleccionar una base de datos que ya existe, sino existe la crea vacia
```mongodb
> use RetailManagementDB
< switched to db RetailManagementDB
```

# Listar las colecciones de la base de datos Seleccionada
```mongodb
> show collections
Customers
new_collection
Orders
Payments
```

# Crear un Indice en la colección
```mongodb
> db.Customers.createIndex({ customer_id: 1 });
customer_id_1

> db.Orders.createIndex({ order_id: 1 });
order_id
```

# Consultar Indices  en la colección
```mongodb
> db.Customers.getIndexes();
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  { v: 2, key: { customer_id: 1 }, name: 'customer_id_1' }
]

> db.Orders.getIndexes();
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  { v: 2, key: { order_id: 1 }, name: 'order_id' }
]
```

# Eliminar Indices
```mongodb
> db.Orders.dropIndex('order_id_1');
{ nIndexesWas: 2, ok: 1 }

> db.Orders.getIndexes();
[
  { v: 2, key: { _id: 1 }, name: '_id_' }
]
```


# Insertar 1 documento de una coleccion
```mongodb
> db.Customers.insertOne({
    customer_id: 1235,
    name: "Maria Lopez",
    age: 30
});

< {
  acknowledged: true,
  insertedId: ObjectId('6717017f928cf000615c3873')
}
```

# Insertar multiples documentos de una coleccion, en un solo query
```mongodb
> db.Customers.insertMany([
    {
        customer_id: 1236,
        name: "Carlos Perez",
        age: 35,
        salary: 2500,     // Este campo está definido
        phone: null,      // Este campo está definido como null
        address: "123 Calle Falsa"
    },
    {
        customer_id: 1237,
        name: "Ana Torres",
        age: 28,
        // salary y phone no están definidos aquí
        address: "456 Avenida Real"
    },
    {
        customer_id: 1238,
        name: "Luis Gonzalez",
        age: 45,
        salary: 3200,     // Este campo está definido
        // phone y address no están definidos aquí
    },
    {
        customer_id: 1239,
        name: "Laura Martinez",
        age: 50,
        salary: null,     // Este campo está definido como null
        phone: null,      // Este campo está definido como null
        address: "789 Plaza Central"
    }
]);


< {
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('67170291928cf000615c3875'),
    '1': ObjectId('67170291928cf000615c3876'),
    '2': ObjectId('67170291928cf000615c3877'),
    '3': ObjectId('67170291928cf000615c3878')
  }
}
```

# Eliminar 1 documento de una coleccion, basado en una condicion
```mongodb
> db.Customers.deleteOne({ customer_id: 0 });

< {
  acknowledged: true,
  deletedCount: 1
}
```

# Eliminar todos documentos de una coleccion, que cumplan la condicion
```mongodb
> db.Customers.deleteMany({ customer_id: { $gt:10 }});

< {
  acknowledged: true,
  deletedCount: 89
}
```

# Actualizar 1 documento de una coleccion, basado en una condicion
```mongodb
> db.Customers.updateOne(
    { customer_id: 1 }, // Criterio de búsqueda
    { $set: { salary: 2222 } } // Campos a actualizar
);

< {
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
```

# Actualizar todos documentos de una coleccion, que cumplan la condicion
```mongodb
> db.Customers.updateMany(
    { salary: { $lt: 3000 } }, // Criterio de búsqueda: salario menor a 3000
    { $inc: { salary: 500 } }  // Incrementar el campo salary en 500
);

< {
  acknowledged: true,
  insertedId: null,
  matchedCount: 4,
  modifiedCount: 4,
  upsertedCount: 0
}
```

# Actualizar todos documentos de una coleccion, que cumplan las condiciones
```mongodb
> db.Customers.updateMany(
    { salary: { $lt: 4000 }, age: { $gt: 40 } },  // Criterio: salario menor a 3000 y edad mayor a 40
    { $mul: { salary: 1.5 } }                     // Multiplicar el campo salary por 1.5
);

< {
  acknowledged: true,
  insertedId: null,
  matchedCount: 3,
  modifiedCount: 3,
  upsertedCount: 0
}
```

# Actualizar o insertar un documentos de una coleccion, que cumplan las condiciones
```mongodb
> db.Customers.updateOne(
    { customer_id: 1234 },  // Criterio de búsqueda
    { 
        $set: { 
            name: "Jorge Cardona", 
            age: 31, 
            nationality: "Unknown" 
        } 
    },  // Campos a actualizar
    { upsert: true }  // Si no encuentra coincidencias, inserta un nuevo documento
);

< {
  acknowledged: true,
  insertedId: ObjectId('6716fe2dc8f95dbf82f9a593'),
  matchedCount: 0,
  modifiedCount: 0,
  upsertedCount: 1
}
```

# Actualizar o insertar un documentos de una coleccion, que cumplan las condiciones
```mongodb
> db.Customers.updateMany(
    { nationality: "Unknown" },       // Criterio de búsqueda
    { $set: { nationality: "Pereira" } }, // Campos a actualizar
    { upsert: true }                  // Insertar si no encuentra coincidencias
);

< {
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
```

# Agregación de Clientes con Órdenes: Inner Join V1
```mongodb
db.Customers.aggregate([
    {
        // Realiza el join entre la colección Customers y Orders
        $lookup: {
            from: "Orders", // Especifica la colección con la que estamos haciendo el join (Orders)
            localField: "customer_id", // Campo en Customers que será usado para el match
            foreignField: "customer_id", // Campo en Orders que será comparado con el campo en Customers
            as: "orders_inner_join_v1" // El resultado del join se guardará en este nuevo campo
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
db.Customers.aggregate([
    {
        // Realiza el join entre la colección Customers y Orders
        $lookup: {
            from: "Orders", // Especifica la colección con la que estamos haciendo el join (Orders)
            localField: "customer_id", // Campo en Customers que será usado para el match
            foreignField: "customer_id", // Campo en Orders que será comparado con el campo en Customers
            as: "orders_inner_join_v1" // El resultado del join se guardará en este nuevo campo
        }
    },
    {
        // Filtra los resultados del join
        $match: {
            "orders_inner_join_v1": { $ne: [] } // Incluye solo los documentos que tienen órdenes, es decir, que no tienen el array vacío
        }
    }
]).explain("executionStats");

# inner join v1, documento anidado conteos antes y despues del join, ademas de todos los documentos
db.Customers.aggregate([
    {
        // Realiza el join entre Customers y Orders
        $lookup: {
            from: "Orders", // Colección Orders con la cual estamos haciendo el join
            localField: "customer_id", // Campo en Customers que se usará para hacer el match
            foreignField: "customer_id", // Campo en Orders con el que se comparará
            as: "orders_inner_join_v3" // Nombre del campo que contendrá las órdenes relacionadas
        }
    },
    {
        $facet: {
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


# INNER JOIN MUESTRA SOLO LOS DOCUMENTOS QUE TIENEN ANDIDADOS ENTRE 2 Y 3 DOCUMENTOS
db.Customers.aggregate([
    {
        // Realiza un join entre la colección Customers y Orders
        $lookup: {
            from: "Orders", // Colección a la que se está uniendo
            localField: "customer_id", // Campo en Customers que se usa para el join
            foreignField: "customer_id", // Campo en Orders que se usa para el join
            as: "orders_inner_join_v1" // Nombre del nuevo campo que contendrá las órdenes
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


# INNER JOIN MUESTRA EL TOTAL DE DOCUMENTOS QUE CUMPLEN CON LA CONSULTA
db.Customers.aggregate([
    {
        $lookup: {
            from: "Orders",
            localField: "customer_id",
            foreignField: "customer_id",
            as: "orders_inner_join_v1"
        }
    },
    {
        $match: {
            "orders_inner_join_v1": { $ne: [] } // Filtra los documentos que tienen orders_inner_join no vacío
        }
    },
    {
        $count: "total_documents" // Cuenta el número total de documentos que cumplen con las condiciones
    }
]);

# INNER JOIN CON CONDICION
db.Customers.aggregate([
    {
        $lookup: {
            from: "Orders",
            localField: "customer_id",
            foreignField: "customer_id",
            as: "orders_inner_join_condition"
        }
    },
    {
        $match: {
            "orders_inner_join_condition": { $ne: [] }, // Filtra los documentos que tienen orders_inner_join no vacío
            "customer_id": 34 // Agrega la condición para customer_id
        }
    }
]);

# INNER Join, v2 documento Relacionado por documento

db.Customers.aggregate([
    {
      $lookup: {
        from: "Orders",
        localField: "customer_id",
        foreignField: "customer_id",
        as: "orders_inner_join_v2"
      }
    },
    {
      $unwind: "$orders_inner_join_v2" // Descompone el array de órdenes en documentos individuales
    },
    {
      $match: {
        "orders_inner_join_v2": { $ne: [] } // Asegura que solo se incluyan los documentos con órdenes
      }
    }
  ]);


# INNER JOIN MUESTRA EL TOTAL DE DOCUMENTOS QUE CUMPLEN CON LA CONSULTA
db.Customers.aggregate([
    {
      $lookup: {
        from: "Orders",
        localField: "customer_id",
        foreignField: "customer_id",
        as: "orders_inner_join_v2"
      }
    },
    {
      $unwind: "$orders_inner_join_v2" // Descompone el array de órdenes en documentos individuales
    },
    {
      $match: {
        "orders_inner_join_v2": { $ne: [] } // Asegura que solo se incluyan los documentos con órdenes
      }
    },
    {
        $count: "total_documents" // Cuenta el número total de documentos que cumplen con las condiciones
    }
  ]);



# INNER Join, v3 documento Relacionado por documento, pero con los campos combinados en un solo documento
db.Customers.aggregate([
    {
        $lookup: {
            from: "Orders",
            localField: "customer_id",
            foreignField: "customer_id",
            as: "orders_inner_join_v3"
        }
    },
    {
        $unwind: "$orders_inner_join_v3" // Descompone el array de órdenes en documentos individuales
    },
    {
        $match: {
            "orders_inner_join_v3": { $ne: [] } // Asegura que solo se incluyan los documentos con órdenes
        }
    },
    {
        $replaceRoot: {
            newRoot: { $mergeObjects: ["$$ROOT", "$orders_inner_join_v3"] } // Combina los campos de Customers y Orders
        }
    },
    {
        $project: {
            orders_inner_join_v3: 0 // Opcional: Si no deseas mostrar el array de órdenes original
        }
    }
]);



# LEFT JOIN

db.Customers.aggregate([
    {
        $lookup: {
            from: "Orders",
            localField: "customer_id",
            foreignField: "customer_id",
            as: "orders_left_join"
        }
    }
]);

# LEFT JOIN, solo los primeros 10 documentos, ordenando por los no vacios primero
db.Customers.aggregate([
    {
        $lookup: {
            from: "Orders",
            localField: "customer_id",
            foreignField: "customer_id",
            as: "orders_left_join"
        }
    },
    {
        $sort: {
            "orders_left_join": -1 // Ordena primero los documentos con orders_left_join no vacío
        }
    },
    {
        $limit: 10 // Limita los resultados a los primeros 10 documentos
    }
]);


# ANTI LEFT JOIN
db.Customers.aggregate([
    {
        $lookup: {
            from: "Orders",                      // La colección con la que estás haciendo el join
            localField: "customer_id",           // Campo en Customers
            foreignField: "customer_id",         // Campo en Orders
            as: "orders_left_join"               // El nombre del campo nuevo donde se guardarán las órdenes
        }
    },


    {
        $match: {
            "orders_left_join": { $eq: [] }     // Filtra para incluir solo los documentos donde el arreglo de órdenes está vacío
        }
    }
]);
