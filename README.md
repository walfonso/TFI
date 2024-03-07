# TRABAJO FINA DE INGENIERIA

##  HR-SIL Sistema de Intermediación Laboral.

Permite manejar el 'State' de una aplicacion, para que sea mas facil mantener conforme va creciendo.
Tambien te ayuda a manejar los datos, conforme el Usuario realiza diferentes acciones.

## Caracteristicas de Redux.

- Solo se tiene un State principal.
- El State cambia de acuerdo a lo que sucede en la interfaz de Usuario.
- Solo ciertas funciones cambian el State.
- El Usuario es el que utiliza estas funciones y cambia el state.
- Solo se realiza un cambio a la vez.

## Principios de Redux.

- Solo existe un Store con todo el State de la Aplicacion.
- Los Componentes / Vistas no modifican el State directamente.
- El State modifica por medio de funciones.
- Store: Contiene el State (Un State por Aplicacion).
- Dispatch: Ejecuta una Accion que actualizara el State.
- Action: Son Objetos (js), tienen un Tipo y un Payload (Datos).
- Subscribe: Similar a un Event Listener para el State.
- Reducers: Funciones, saben que hacer con las Acciones y el Payload.

![image](https://user-images.githubusercontent.com/24545141/140233398-09735dd7-71aa-4cc0-926b-3710d0b59045.png)

## ¿Como instalar la Aplicacion?

```sh


```

## ¿Como correr Localmente la Aplicacion?

```sh
python manage.py runserver
```

## Vista Online

View the hosted on [Heroku] (https://dbmarket2023-1d0af4cbfaaf.herokuapp.com/)

## Desarrollo de Front-End

### Walter Alfonso: recurso `product`

- Acceso a los métodos CRUD - MongoDB:

1. -> \_DashBoard
   ![Dasboard](https://raw.githubusercontent.com/bonino97/FE-MCGA/products/src/assets/dashboard.png)

2. -> _Productos - Lista de todos los productos_
   ![List Products](https://raw.githubusercontent.com/bonino97/FE-MCGA/products/src/assets/products.png)

3. -> _Productos - Agregar producto_
   ![Add Product](https://raw.githubusercontent.com/bonino97/FE-MCGA/products/src/assets/addProduct.png)

4. -> _Productos - Actualizar datos del producto_
   ![Edit Product](https://raw.githubusercontent.com/walfonso/MCGA-FE/development/src/assets/updateProduct.png)

5. -> _Productos - Borrar producto_

CRUD Usuarios

1. -> _Usuarios - Lista de todos los usuarios_
   ![List Products](https://raw.githubusercontent.com/walfonso/MCGA-FE/development/src/assets/users.png)

2. -> _Usuarios - Agregar usuario_
   ![Add Product](https://raw.githubusercontent.com/walfonso/MCGA-FE/development//src/assets/addUser.png)

3. -> _Productos - Actualizar datos del producto_
   ![Edit Product](https://raw.githubusercontent.com/walfonso/MCGA-FE/development/src/assets/updateProduct.png)

4. -> _Usuarios - Borrar usuario_

LOGIN Usuarios

1.  -> _Acceso Usuarios - Login usuario_
    ![Edit Product](https://raw.githubusercontent.com/walfonso/MCGA-FE/development/src/assets/login.png)

Walter Alfonso

© Año 2023

