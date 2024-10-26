## data-collection-json-csv-sql
data-collection-json-csv-sql is a repository dedicated to storing a variety of datasets in both JSON, SQL and CSV formats. This collection includes data from different domains and can be used for data analysis, machine learning projects, or educational purposes.

## Usa el Método  para Resultados Organizados
El método  se utiliza en MongoDB para presentar los resultados de las consultas de manera más legible y estructurada. Esto es especialmente útil cuando se recuperan datos de APIs o se realizan consultas que devuelven varios documentos. Al aplicar , los resultados se formatean con saltos de línea y sangrías, lo que facilita su visualización.

```mongodb

```
## Beneficios de Usar 
Legibilidad: Mejora la claridad al presentar documentos con varios campos.
Estructura: Permite identificar rápidamente la jerarquía de los datos.
Facilidad de Análisis: Ayuda a los desarrolladores a entender mejor la salida de las consultas.

Sí, exactamente. El método `.pretty()` se utiliza principalmente para mejorar la legibilidad de los resultados de las consultas que devuelven un cursor, como:

### Métodos donde se puede usar `.pretty()`
El método .pretty() se utiliza principalmente para mejorar la legibilidad de los resultados de las consultas que devuelven un cursor, como:

1. **`find()`**:
   - Para visualizar documentos en una colección de manera legible.
   ```mongodb
   db.Customers.find().pretty();
   ```

2. **`aggregate()`**:
   - Para mostrar los resultados de las operaciones de agregación con un formato estructurado.
   ```mongodb
   db.Customers.aggregate([...]).pretty();
   ```

# <center> BASES DE DATOS Y COLECCIONES
## Crear bases de datos
```mongodb
use test_db;  // Cambia el contexto de la base de datos a 'test_db'
```
<img src="images\01_create_database.png">

## Crear una coleccion
```mongodb
db.createCollection('test_collection');  // Crea una nueva colección llamada 'test_collection' en la base de datos actual
// { ok: 1 }  // Mensaje de confirmación que indica que la colección se ha creado correctamente (ok: 1)
```
<img src="images\02_create_collection.png">

## Listar las bases de datos, sino tiene colecciones no se Lista
```mongodb
show databases;  // Muestra una lista de todas las bases de datos disponibles en el servidor MongoDB 
```
<img src="images\03_show_databases.png">

## Eliminar una coleccion
```mongodb
db.test_collection.drop();  // Elimina la colección llamada 'test_collection' de la base de datos actual
```
<img src="images\04_drop_collection.png">

## Eliminar una base de datos
```mongodb
db.dropDatabase();  // Elimina la base de datos actual (test_db) junto con todas sus colecciones
```
<img src="images\05_drop_database.png">

## Seleccionar una base de datos que ya existe, sino existe la crea vacia
```mongodb
use RetailManagementDB;  // Cambia el contexto de la base de datos a 'RetailManagementDB'
```
<img src="images\06_change_database.png">

## Listar las colecciones de la base de datos Seleccionada
```mongodb
show collections;  // Muestra una lista de todas las colecciones disponibles en la base de datos actual (RetailManagementDB)
```
<img src="images\07_show_collections.png">

# <center> INDICES
## Crear un Indice generico en la colección
```mongodb
db.Customers.createIndex({
    customer_id: 1  // Crea un índice ascendente en el campo customer_id en la colección Customers
});
```
<img src="images\08_create_generic_index.png">


## Crear un Indice con nombre personalizado en la colección
```mongodb
db.Orders.createIndex(
    { customer_id: 1 },          // Crea un índice ascendente en el campo customer_id en la colección Orders
    { name: "idx_customer_id" }  // Nombre personalizado asignado al índice: idx_customer_id
);
```
<img src="images\09_create_custom_name_index.png">

## Crear un multiples indices en la colección
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

## Consultar Indices  en la colección
```mongodb
db.Customers.getIndexes();
```
<img src="images\11_check_all_indexes.png">

## Elimina todos los indices presentes en la colección excepto _id
```mongodb
db.Payments.dropIndexes().; // Elimina todos los índices excepto _id
```
<img src="images\12_drop_all_indexes.png">

## Eliminar Indices
```mongodb
db.Orders.dropIndex('order_id_1');  // Elimina el índice llamado 'order_id_1' de la colección Orders
```
<img src="images\13_drop_one_index.png">

# <center> INSERCION DE DOCUMENTOS
## Insertar 1 documento de una coleccion
```mongodb
db.Customers.insertOne({  // Inserta un nuevo documento en la colección Customers
    customer_id: 1235,      // Campo que representa el ID del cliente
    name: "Nathalie Cardona", // Campo que representa el nombre del cliente
    age: 30                 // Campo que representa la edad del cliente
});
```
<img src="images\14_insert_one.png">

## Insertar multiples documentos de una coleccion, en un solo query
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

# <center> ELIMINACION DE DOCUMENTOS
## Eliminar 1 documento de una coleccion, basado en una condicion
```mongodb
db.Customers.deleteOne(  // Elimina un documento de la colección Customers que coincide con el criterio especificado
    { customer_id: 0 }     // Criterio de búsqueda: busca un documento donde customer_id sea igual a 0
);
```
<img src="images\16_delete_one.png">

## Eliminar todos documentos de una coleccion, que cumplan la condicion
```mongodb
db.Customers.deleteMany(  // Elimina múltiples documentos de la colección Customers que coinciden con el criterio especificado
    { customer_id: { $gt: 10 }}  // Criterio de búsqueda: busca documentos donde customer_id sea mayor que 10
);

db.Orders.deleteMany(  // Inicia la operación para eliminar múltiples documentos de la colección Orders
    { 
        $or: [  // Utiliza el operador lógico OR para combinar condiciones
            { customer_id: { $lt: 5 } },    // Elimina documentos donde customer_id sea menor que 5
            { customer_id: { $gt: 15 } }    // Elimina documentos donde customer_id sea mayor que 15
        ]  
    }
);
```
<img src="images\17_delete_many.png">

# <center> ACTUALIZACION DE DOCUMENTOS
## Actualizar 1 documento de una coleccion, basado en una condicion
```mongodb
db.Customers.updateOne(  // Actualiza un único documento en la colección Customers que coincide con el criterio especificado
    { customer_id: 1 },    // Criterio de búsqueda: busca un documento donde customer_id sea igual a 1
    { $set: { salary: 2222 } }  // Actualiza el campo salary, estableciendo su valor en 2222
);
```
<img src="images\18_update_one.png">

## Actualizar todos documentos de una coleccion, que cumplan la condicion
```mongodb
db.Customers.updateMany(  // Actualiza múltiples documentos en la colección Customers que coinciden con el criterio especificado
    { salary: { $lt: 3000 } }, // Criterio de búsqueda: busca documentos donde el salario sea menor a 3000
    { $inc: { salary: 500 } }  // Incrementa el campo salary en 500 para todos los documentos que coinciden
);
```
<img src="images\19_update_many_1.png">

## Actualizar todos documentos de una coleccion, que cumplan las condiciones
```mongodb
db.Customers.updateMany(  // Actualiza múltiples documentos en la colección Customers que coinciden con el criterio especificado
    { salary: { $lt: 4000 }, age: { $gt: 40 } },  // Criterio de búsqueda: busca documentos donde el salario sea menor a 4000 y la edad mayor a 40
    { $mul: { salary: 1.5 } }                     // Multiplica el campo salary por 1.5 para todos los documentos que coinciden
);
```
<img src="images\20_update_many_2.png">

# <center> UPSERT - ACTUALIZACION/INSERCION DE DOCUMENTOS
## UPSERT Actualizar o insertar un documentos de una coleccion, que cumplan las condiciones
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

## UPSERT Actualizar o insertar un documentos de una coleccion, que cumplan las condiciones
```mongodb
db.Customers.updateMany(  // Actualiza múltiples documentos en la colección Customers que coinciden con el criterio especificado
    { nationality: "Unknown" },       // Criterio de búsqueda: busca documentos donde la nacionalidad sea "Unknown"
    { $set: { nationality: "Pereira" } }, // Actualiza el campo nationality, estableciendo su valor en "Pereira"
    { upsert: true }                  // Opción upsert: si no encuentra coincidencias, inserta un nuevo documento
);
```
<img src="images\22_upsert_many.png">

# <center> CONSULTA DE DOCUMENTOS
## recuperar el primer documento de la coleccion
```mongodb
db.Customers.findOne(); // Utiliza el método findOne() para obtener el primer documento de la colección Customers.
```
<img src="images\23_find_one.png">


## recuperar todos los documentos de la coleccion
```mongodb
db.Customers.find(); // Usa el método find() para obtener todos los documentos de la colección Customers.
```
<img src="images\24_find_all.png">

## Recuperar los primeros 2 documentos de la colección
## Utiliza el método find() para obtener todos los documentos de la colección Customers,
## y luego aplica limit(2) para devolver solo los primeros dos documentos.
```mongodb
db.Customers.find().limit(2).pretty();
```
<img src="images\25_find_limit.png">

# <center> CONTEO DE DOCUMENTOS
## Contar cuántos documentos hay en la colección Customers
## Utiliza el método countDocuments() para devolver el número total de documentos en la colección.
```mongodb
// Cuenta el número total de documentos en la colección Customers
db.Customers.countDocuments();
```
<img src="images\26_count.png">

## Contar cuántos documentos hay en la colección Customers con la condicion dada
```mongodb
// Cuenta el número de clientes que tienen más de 30 años
db.Customers.countDocuments({ age: { $gt: 30 } });
```
<img src="images\27_condition_count.png">

# <center> CONSULTA Y LIMITE DE DOCUMENTOS CON CAMPOS ESPECIFICOS
## Recuperar todos los documentos pero mostrando solo los primeros tres campos (_id, customer_id, name)
## Utiliza el método find() y la proyección para incluir solo los campos deseados.
```mongodb
db.Customers.find({}, { _id: 1, customer_id: 1, name: 1 }).limit(4)
```
<img src="images\28_filter_equals.png">

## Recuperar todos los documentos menores que la condicion
```mongodb
db.Customers.find(
    {
        'customer_id': { $lt: 2 } // Filtro de búsqueda: Busca documentos donde el campo 'customer_id' sea menor que 2
    }
);
```
<img src="images\29_filter_lower_than.png">

# <center> CONSULTA DE DOCUMENTOS CON CONDICION MENOR O IGUAL QUE
## Recuperar todos los documentos menores o iguales que la condicion
```mongodb
db.Customers.find(
    {
        'customer_id': { $lte: 2 } // Filtro de búsqueda: Busca documentos donde el campo 'customer_id' sea menor o igual a 2
    }
);
```
<img src="images\30_filter_lower_or_equals_than.png">

# <center> CONSULTA DE DOCUMENTOS CON CONDICION MENOR QUE
## Recuperar todos los documentos mayores que la condicion
```mongodb
db.Customers.find(
    {
        'customer_id': { $gt: 10 } // Filtro de búsqueda: Busca documentos donde el campo 'customer_id' sea mayor que 10
    }
);
```
<img src="images\31_filter_greater_than.png">

# <center> CONSULTA DE DOCUMENTOS CON CONDICION OR
## Recuperar todos los documentos que cumplan la condicion del or
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

# <center> CONSULTA DE DOCUMENTOS CON CONDICION AND
## Recuperar todos los documentos que cumplan la condicion del and
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

# <center> CONSULTA DE DOCUMENTOS CON CONDICIONES AND y OR
## Recuperar todos los documentos que cumplan la condicion del and y el or
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


## Recuperar todos los documentos que cumplan la condicion del and y ordenarlo de manera descendete
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

# <center> AGREGACIONES

## Agrupacion, agregado, Recuperar todos los documentos agrupados y ordenados segun la condicion
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


# BUSQUEDA POR TEXTO
## Solo busca por documentos que COMIENCEN por una cadena o caracter especifico
### SENSIBLE AL CASO
```mongodb
db.Customers.find({
  name: { $regex: "^m" }  // Busca documentos donde el campo "name" comience con la letra "M"
});
```

### INSENSIBLE AL CASO
```mongodb
db.Customers.find({
  name: { $regex: "^m" , $options: "i"}  // Busca documentos donde el campo "name" comience con la letra "m",  La opción "i" hace que la búsqueda sea insensible a mayúsculas/minúsculas
});
```
<img src="images\37_case_insensitive_prefix_match.png">

## Solo busca por documentos que CONTIENEN la una cadena o caracter especifico
### SENSIBLE AL CASO
```mongodb
db.Customers.find({
  name: { $regex: "st" }  // Busca documentos donde el campo "name" contenga la secuencia de caracteres "st"
});
```

### INSENSIBLE AL CASO
```mongodb
db.Customers.find({
  name: { $regex: "st", $options: "i" } // Busca documentos donde el campo "name" contenga la secuencia de caracteres "st"
});
```
<img src="images\38_case_insensitive_contains_match.png">

## Solo busca por documentos que FINALICEN por una cadena o caracter especifico
### SENSIBLE AL CASO
```mongodb
db.Customers.find({
  email: { $regex: ".NET$" }  // Busca documentos donde el campo "email" finalice la secuencia de caracteres ".NET"
});
```

### INSENSIBLE AL CASO
```mongodb
db.Customers.find({
  email: { $regex: ".NET$", $options: "i" } // Busca documentos donde el campo "email" finalice la secuencia de caracteres ".NET", NO SENSIBLE AL CASO
});
```
<img src="images\39_case_insensitive_suffix_match.png">


## Busca el PRIMER DOCUMENTO y lo elimina
```mongodb
db.Orders.findOneAndDelete({ 
  order_id: { $lt: 4 }  // Busca y elimina el primer documento donde "order_id" sea menor que 4
});
```
<img src="images\40_findOne_and_delete.png">


## Busca el PRIMER DOCUMENTO y lo Reemplaza
```mongodb
db.Customers.findOneAndReplace(
  { customer_id: 1 },  // Filtro para encontrar el documento
  { 
    customer_id: 1,               // Nuevo documento
    name: "Ernest Boyd",
    email: "jeffreyday@example.org",
    phone: "249.965.2201",
    address: "10955 Roy Canyon Apt. 553 Jeanetteland, AS 54699",
    age: 83,
    country: "Romania",
    continent: "Asia"
  },
  { returnNewDocument: true }  // Opcional: retorna el nuevo documento
);
```
<img src="images\41_findOne_and_replace.png">


## Busca el PRIMER DOCUMENTO y lo Actualiza
```mongodb
db.Customers.findOneAndUpdate(
  { customer_id: 1 },  // Filtro para encontrar el documento
  { 
    $set: {              // Modifica solo los campos especificados
      email: "newemail@example.com",  // Cambia el email
      age: 23                       // Actualiza la edad
    }
  },
  { returnNewDocument: true }  // Opcional: retorna el documento actualizado
);
```
<img src="images\42_findOne_and_update.png">


## Busca los valores UNICOS del campo
```mongodb
db.Customers.distinct("current_continent");  // // Busca y devuelve una lista de valores únicos del campo  current_continent
```
<img src="images\43_distinct.png">


## OBTENER EL ULTIMO VALOR DE UN CAMPO QUE CONTIENE UNA LISTA USANDO FIND 
```mongodb
db.Payments.find(
  {},
  { currency: { $slice: -1 } }  // Proyección para obtener solo el último valor de currency en cada documento
).sort({ _id: -1 })  // Ordena por _id en orden descendente para obtener los últimos documentos
.limit(3);  // Limita la salida a los 3 últimos documentos
```
<img src="images\44_getLastCurrencyValueFromList_find.png">

## OBTENER EL ULTIMO VALOR DE UN CAMPO QUE CONTIENE UNA LISTA USANDO AGGREGATE
```mongodb
db.Payments.aggregate([
  {
    $sort: { _id: -1 }  // Ordena los documentos por _id en orden descendente
  },
  {
    $limit: 3  // Limita la salida a los 3 últimos documentos
  },
  {
    $project: {
      _id: 1,  // Incluye el ID del documento
      order_id: 1,  // Incluye otros campos que desees
      last_currency: { $arrayElemAt: ["$currency", -1] }  // Obtiene el último valor de currency
    }
  }
])
```
<img src="images\45_getLastCurrencyValueFromList_agreagate.png">

## OBTENER LOS DOCUMeNTOS QUE TIENEN UN VALOR DENTRO DE UNA LISTA SENSITIVO AL CASO
```mongodb
db.Payments.aggregate([
  {
    $match: { currency: { $in: ["Singapore dollar"] } }  // Filtra documentos donde currency incluye "Singapore dollar"
  }
])
```
<img src="images\46_check_value_in_list_sensitive.png">


## OBTENER LOS DOCUMeNTOS QUE TIENEN UN VALOR DENTRO DE UNA LISTA NO SENSITIVO AL CASO
```mongodb
db.Payments.find({
  currency: { $regex: /^singapore dollar$/i }  // Busca "Singapore dollar" en el campo currency sin ser sensible al caso
})
```
<img src="images\47_check_value_in_list_no_sensitive_case.png">

## MAP REDUCE
```mongodb
// Función Map: define una función para mapear los datos de entrada
var mapFunction = function() {
    // Emitimos el campo 'payment_method' como clave y el campo 'amount' como valor
    emit(this.payment_method, this.amount);
};

// Función Reduce: define una función para reducir los datos mapeados
var reduceFunction = function(key, values) {
    // Suma todos los valores de 'amount' que tienen la misma clave 'payment_method'
    return Array.sum(values);
};

// Ejecución del MapReduce sobre la colección 'Payments'
db.Payments.mapReduce(
    // Especifica la función map para procesar cada documento de la colección
    mapFunction,
    
    // Especifica la función reduce para agrupar y consolidar los resultados
    reduceFunction,
    
    {
        // Define la colección de salida, donde se guardarán los resultados agrupados
        out: "map_reduce_payment_collection"
    }
);

// Consulta la colección de salida 'map_reduce_payment_collection' para ver los resultados generados
db.map_reduce_payment_collection.find();
```

## MAP REDUCE Incluyendo multiples map/reduce
```mongodb

// Comando para eliminar todos los documentos de la colección 'map_reduce_payment_collection'
db.map_reduce_payment_collection.deleteMany({});

var mapFunction = function() {
    // Dividir la fecha en año, mes y día.
    // La fecha está en formato "YYYY-MM-DD", por lo que utilizamos split para separarla.
    var dateParts = this.payment_date.split("-");

    // Asignar el primer elemento del array a la variable 'year', que representa el año.
    var year = dateParts[0];

    // Asignar el segundo elemento del array a la variable 'month', que representa el mes.
    var month = dateParts[1];

    // Asignar el tercer elemento del array a la variable 'day', que representa el día.
    var day = dateParts[2];

    // Emitir el payment_method como clave en el resultado del map.
    // Emitimos un objeto que incluye el año, mes, día, el monto de la transacción (amount),
    // y un conteo inicial de 1 para esta transacción.
    emit(this.payment_method, {
        year: year,    // Año extraído de la fecha
        month: month,  // Mes extraído de la fecha
        day: day,      // Día extraído de la fecha
        amount: this.amount, // Monto de la transacción
        count: 1       // Inicializamos el conteo en 1 para cada transacción
    });
};

var reduceFunction = function(key, values) {
    // Inicializamos un objeto 'reducedValue' para almacenar el monto total,
    // el conteo total y un objeto para contar las ocurrencias de cada fecha.
    var reducedValue = {
        totalAmount: 0,   // Total acumulado de los montos
        totalCount: 0,    // Total acumulado de las transacciones
        dates: {}         // Objeto para contar las ocurrencias de cada fecha
    };

    // Iteramos sobre cada valor en el array 'values', que contiene los resultados emitidos por la función map.
    values.forEach(function(value) {
        // Sumar los montos de cada transacción al total acumulado.
        reducedValue.totalAmount += value.amount;

        // Sumar la cantidad de transacciones al conteo total.
        reducedValue.totalCount += value.count;

        // Crear un identificador único para la fecha en formato "YYYY-MM-DD".
        var dateKey = value.year + "-" + value.month + "-" + value.day;

        // Si la fecha no está en el objeto 'dates', inicializarla en 0.
        if (!reducedValue.dates[dateKey]) {
            reducedValue.dates[dateKey] = 0; // Inicializa el conteo de esa fecha
        }

        // Aumentar el conteo para la fecha correspondiente.
        reducedValue.dates[dateKey] += value.count; // Aumentar el conteo para esta fecha
    });

    // Retornar el objeto 'reducedValue' que ahora contiene el monto total,
    // el conteo total y un objeto con las fechas y sus ocurrencias.
    return reducedValue;
};

// Ejecución del MapReduce sobre la colección 'Payments'
db.Payments.mapReduce(
    // Especifica la función map para procesar cada documento de la colección
    mapFunction,
    
    // Especifica la función reduce para agrupar y consolidar los resultados
    reduceFunction,
    
    {
        // Define la colección de salida, donde se guardarán los resultados agrupados
        out: "map_reduce_payment_collection"
    }
);

// Consulta la colección de salida 'map_reduce_payment_collection' para ver los resultados generados
db.map_reduce_payment_collection.find();
```

<img src="images\48_map_reduce.png">

# <center> JOINs
## Inner Join V1
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
<img src="images\49_inner_join_collections.png">

## INNER JOIN ENTRE MUTIPLES COLECCIONES INICIANDO DESDE EL 4 DOCUMENTO Y FILTRANDO LOS 2 SIGUIENTES
```mongodb
db.Customers.aggregate([
    {
        // Realiza el join entre la colección Customers y Orders
        $lookup: {
            from: "Orders",              // Especifica la colección con la que estamos haciendo el join (Orders)
            localField: "customer_id",   // Campo en Customers que será usado para el match
            foreignField: "customer_id",  // Campo en Orders que será comparado con el campo en Customers
            as: "customers_orders_inner_join" // El resultado del join se guardará en este nuevo campo
        }
    },
    {
        // Filtra los resultados del join para incluir solo los documentos que tienen órdenes
        $match: {
            "customers_orders_inner_join": { $ne: [] } // Incluye solo los documentos donde el array no está vacío
        }
    },
    {
        // Realiza el join entre la colección Orders y Payments
        $lookup: {
            from: "Payments",               // Especifica la colección con la que estamos haciendo el join (Payments)
            localField: "customers_orders_inner_join.order_id", // Campo en Orders que será usado para el match
            foreignField: "order_id",       // Campo en Payments que será comparado con el campo en Orders
            as: "payments_orders_inner_join" // El resultado del join se guardará en este nuevo campo
        }
    },
    {
        // Filtra los resultados del segundo join para incluir solo los documentos que tienen pagos
        $match: {
            "payments_orders_inner_join": { $ne: [] } // Incluye solo los documentos donde el array no está vacío
        }
    },
    {
        // Salta los primeros 3 documentos del resultado
        $skip: 3  // Este operador omite los primeros 3 documentos
    },
    {
        // Limita la salida a los siguientes 2 documentos después del skip
        $limit: 2  // Este operador limita el resultado a los siguientes 2 documentos
    }
]);
```

<img src="images\50_inner_join_multiple_collections.png">

## INNER JOIN V1, y PLAN DE EJECUCION
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

## INNER JOIN V1, documento anidado conteos antes y despues del join, ademas de todos los documentos
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

## INNER JOIN V1 MUESTRA SOLO LOS DOCUMENTOS QUE TIENEN ANDIDADOS ENTRE 2 Y 3 DOCUMENTOS
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

## INNER JOIN V1 MUESTRA EL TOTAL DE DOCUMENTOS QUE CUMPLEN CON LA CONSULTA
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

## INNER JOIN CON CONDICION
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

## INNER JOIN V2 documento Relacionado por documento
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

## INNER JOIN V2 MUESTRA EL TOTAL DE DOCUMENTOS QUE CUMPLEN CON LA CONSULTA
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


## INNER JOIN V3 documento Relacionado por documento, pero con los campos combinados en un solo documento
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

## LEFT JOIN
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

## LEFT JOIN, solo los primeros 10 documentos, ordenando por los no vacios primero
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

## ANTI LEFT JOIN
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

## RIGHT JOIN, se invierten las colecciones del left join
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

## ANTI RIGHT JOIN
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

## FULLOUTER JOIN V1 CON DOCUMENTOS ANIDADOS
```mongodb
db.Customers.aggregate([
    {
        // Realiza un Left Join entre Customers y Orders
        $lookup: {
            from: "Orders",                   // Colección con la que se hace el join
            localField: "customer_id",        // Campo en Customers para el match
            foreignField: "customer_id",      // Campo en Orders para el match
            as: "left_join"                   // Resultado del left join se guarda aquí
        }
    },
    {
        // Agrega el resultado de las órdenes que no tienen clientes
        $unionWith: {
            // Realiza un Right Join entre Orders y Customers
            coll: "Orders",
            pipeline: [
                {
                    $lookup: {
                        from: "Customers",            // Colección con la que se hace el join
                        localField: "customer_id",    // Campo en Orders para el match
                        foreignField: "customer_id",   // Campo en Customers para el match
                        as: "right_join"              // Resultado del right join se guarda aquí
                    }
                }
            ]
        }
    }
]);
```

## FULLOUTER JOIN V2 SIN DOCUMENTOS ANIDADOS, PERO JSON DE LA COLECCION DEL JOIN
```mongodb
db.Customers.aggregate([  // Inicia una operación de agregación en la colección Customers
    {
        $lookup: {  // Realiza un Left Join entre Customers y Orders
            from: "Orders",                  // Colección a la que se está uniendo
            localField: "customer_id",       // Campo en Customers que se usa para el join
            foreignField: "customer_id",     // Campo en Orders que se usa para el join
            as: "orders"                      // Nombre del nuevo campo que contendrá las órdenes
        }
    },
    {
        $unionWith: {  // Realiza un Right Join para obtener las órdenes sin clientes
            coll: "Orders",
            pipeline: [
                {
                    $lookup: {
                        from: "Customers",            // Colección a la que se está uniendo
                        localField: "customer_id",    // Campo en Orders que se usa para el join
                        foreignField: "customer_id",   // Campo en Customers que se usa para el join
                        as: "customer"                 // Nombre del nuevo campo que contendrá el cliente
                    }
                },
                {
                    $project: {  // Proyecta solo los campos necesarios
                        order_id: 1, // Campo de la orden que se desea incluir
                        order_date: 1, // Otro campo de la orden
                        // Agrega aquí otros campos de Orders que deseas incluir
                        customer: { $arrayElemAt: ["$customer", 0] } // Asegura que solo se incluya el primer cliente
                    }
                }
            ]
        }
    },
    {
        $replaceRoot: {  // Reemplaza la raíz del documento
            newRoot: { 
                $mergeObjects: [ "$$ROOT", { orders: "$orders", customer: "$customer" } ] // Combina los campos
            }
        }
    }
]);
```

## FULLOUTER JOIN V3 SIN DOCUMENTOS ANIDADOS, TODOS LOS CAMPOS AL MISMO NIVEL
```mongodb
db.Customers.aggregate([  // Inicia una operación de agregación en la colección Customers
    {
        $lookup: {  // Realiza un Left Join entre Customers y Orders
            from: "Orders",                  // Colección a la que se está uniendo
            localField: "customer_id",       // Campo en Customers que se usa para el join
            foreignField: "customer_id",     // Campo en Orders que se usa para el join
            as: "orders"                      // Nombre del nuevo campo que contendrá las órdenes
        }
    },
    {
        $unwind: {  // Descompone el array de órdenes en documentos individuales
            path: "$orders",
            preserveNullAndEmptyArrays: true  // Mantiene documentos de Customers sin órdenes
        }
    },
    {
        $unionWith: {  // Realiza un Right Join para obtener las órdenes sin clientes
            coll: "Orders",
            pipeline: [
                {
                    $lookup: {
                        from: "Customers",            // Colección a la que se está uniendo
                        localField: "customer_id",    // Campo en Orders que se usa para el join
                        foreignField: "customer_id",   // Campo en Customers que se usa para el join
                        as: "customer"                 // Nombre del nuevo campo que contendrá el cliente
                    }
                },
                {
                    $unwind: {                     // Descompone el array de clientes en documentos individuales
                        path: "$customer",
                        preserveNullAndEmptyArrays: true // Mantiene documentos de Orders sin clientes
                    }
                }
            ]
        }
    },
    {
        $replaceRoot: {  // Reemplaza la raíz del documento
            newRoot: { 
                $mergeObjects: [ "$$ROOT", "$orders", "$customer" ] // Combina todos los campos
            }
        }
    },
    {
        $sort: { 
            customer_id: 1, // Ordena los resultados por customer_id en orden ascendente
            order_id: 1     // Ordena los resultados por order_id en orden ascendente
        }
    },
    {
        $project: {
            orders: 0, // Opcional: Si no deseas mostrar el campo de órdenes como array
            customer: 0 // Opcional: Si no deseas mostrar el campo de cliente como objeto
        }
    }
]);
```

## FULLOUTER JOIN V3 SIN DOCUMENTOS ANIDADOS, TODOS LOS CAMPOS AL MISMO NIVEL ADICIONANDO EL ID DE AMBOS OBJETOS
```mongodb
db.Customers.aggregate([  // Inicia una operación de agregación sobre la colección "Customers"
    {
        $lookup: {  // Realiza un Left Join entre la colección "Customers" y "Orders"
            from: "Orders",  // Colección "Orders" a la que se va a unir
            localField: "customer_id",  // Campo en "Customers" que se usará para la coincidencia
            foreignField: "customer_id",  // Campo en "Orders" que se usará para la coincidencia
            as: "orders"  // Almacena los documentos coincidentes de "Orders" en el campo "orders"
        }
    },
    {
        $unwind: {  // Descompone el array "orders" en documentos individuales para trabajar con ellos uno por uno
            path: "$orders",  // Descompone el campo "orders"
            preserveNullAndEmptyArrays: true  // Si no hay órdenes coincidentes, mantiene el documento de "Customers" sin modificaciones
        }
    },
    {
        $unionWith: {  // Realiza una operación de "Right Join" para incluir órdenes que no tengan clientes
            coll: "Orders",  // Trabaja con la colección "Orders"
            pipeline: [  // Define un pipeline (flujo de operaciones) para procesar los documentos de "Orders"
                {
                    $lookup: {  // Realiza un Join entre "Orders" y "Customers" para encontrar clientes
                        from: "Customers",  // Colección "Customers" a la que se va a unir
                        localField: "customer_id",  // Campo en "Orders" que se usará para la coincidencia
                        foreignField: "customer_id",  // Campo en "Customers" que se usará para la coincidencia
                        as: "customer"  // Almacena los documentos coincidentes de "Customers" en el campo "customer"
                    }
                },
                {
                    $unwind: {  // Descompone el array "customer" en documentos individuales
                        path: "$customer",  // Descompone el campo "customer"
                        preserveNullAndEmptyArrays: true  // Si no hay clientes coincidentes, mantiene el documento de "Orders" sin modificaciones
                    }
                }
            ]
        }
    },
    {
        $addFields: {  // Añade nuevos campos al resultado sin eliminar los campos originales
            _id_Customer: { 
                $cond: { 
                    if: { $ne: ["$customer", null] },  // Si el campo "customer" no es null (existe cliente asociado)
                    then: "$customer._id",  // Asigna el ID del cliente al nuevo campo "_id_Customer"
                    else: null  // Si no hay cliente asociado, asigna null a "_id_Customer"
                } 
            },
            _id_Order: { 
                $cond: { 
                    if: { $ne: ["$orders", null] },  // Si el campo "orders" no es null (existe orden asociada)
                    then: "$orders._id",  // Asigna el ID de la orden al nuevo campo "_id_Order"
                    else: null  // Si no hay orden asociada, asigna null a "_id_Order"
                }
            }
        }
    },
    {
        $replaceRoot: {  // Reemplaza la raíz del documento actual por una combinación de varios campos
            newRoot: { 
                $mergeObjects: [ "$$ROOT", "$customer", "$orders"]  // Combina todos los campos de $$ROOT (el documento original), "customer" y "orders" en un único documento
            }
        }
    },
    {
        $sort: {  // Ordena los resultados de la agregación
            customer_id: 1,  // Orden ascendente por el campo "customer_id"
            order_id: 1  // Orden ascendente por el campo "order_id"
        }
    },
    {
        $project: {  // Controla qué campos se mostrarán en los resultados finales
            orders: 0,  // Elimina el campo "orders" del resultado
            customer: 0  // Elimina el campo "customer" del resultado
        }
    }
]);
```

## ANTI FULLOUTER JOIN
```mongodb
db.Customers.aggregate([
    {
        // Realiza un Left Join entre Customers y Orders
        $lookup: {
            from: "Orders",                   // Colección con la que se hace el join
            localField: "customer_id",        // Campo en Customers para el match
            foreignField: "customer_id",      // Campo en Orders para el match
            as: "orders_anti_left_join"       // Resultado del left join se guarda aquí
        }
    },
    {
        // Filtra para incluir solo los clientes que no tienen órdenes
        $match: {
            "orders_anti_left_join": { $eq: [] }  // Clientes sin órdenes
        }
    },
    {
        // Agrega el resultado de los clientes sin órdenes en un array
        $unionWith: {
            // Realiza un Right Join entre Orders y Customers
            coll: "Orders",
            pipeline: [
                {
                    $lookup: {
                        from: "Customers",            // Colección con la que se hace el join
                        localField: "customer_id",    // Campo en Orders para el match
                        foreignField: "customer_id",   // Campo en Customers para el match
                        as: "orders_anti_right_join"   // Resultado del right join se guarda aquí
                    }
                },
                {
                    // Filtra para incluir solo las órdenes que no tienen clientes
                    $match: {
                        "orders_anti_right_join": { $eq: [] }  // Órdenes sin clientes
                    }
                }
            ]
        }
    },
    {
        // Proyecta todos los campos menos orders_anti_left_join y orders_anti_right_join
        $project: {
            orders_anti_left_join: 0,      // Excluye el campo orders_anti_left_join que es una lista vacia
            orders_anti_right_join: 0,     // Excluye el campo orders_anti_right_join  que es una lista vacia
        }
    }
]);
```

## UNION ALL
```mongodb
db.Customers.aggregate([
    // 1. Incluye todos los documentos de Customers
    {
        $unionWith: {
            coll: "Orders",  // Une Customers con la colección Orders
        }
    }
]);
```

## UNION ALL MULTIPLES COLECCIONES
```mongodb
db.Customers.aggregate([
    // 1. Une los documentos de Customers con los de Orders
    {
        $unionWith: {
            coll: "Orders",  // Especifica que se unirá con la colección Orders
        }
    },
    // 2. Une los documentos de las colecciones anteriores con los de Payments
    {
        $unionWith: {
            coll: "Payments",  // Especifica que se unirá con la colección Payments
        }
    }
]);
```

## UNION
```mongodb
db.Customers.aggregate([
    // 1. Incluye todos los documentos de Customers
    {
        $unionWith: {
            coll: "Orders"  // Une Customers con la colección Orders
        }
    },
    // 2. Agrupa para eliminar duplicados, validando por múltiples campos
    {
        $group: {
            _id: {
                customer_id: "$customer_id",  // Campo para identificar duplicados
                email: "$email",               // Otro campo para validar duplicados
                // Agrega más campos según sea necesario
            },
            doc: { $first: "$$ROOT" }  // Mantiene el primer documento encontrado
        }
    },
    // 3. Reemplaza la raíz con el documento original
    {
        $replaceRoot: { newRoot: "$doc" }
    },
    // 4. Ordena los resultados por customer_id de forma ascendente
    {
        $sort: { customer_id: 1 }  // 1 para orden ascendente
    }
]);
```