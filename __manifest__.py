# -*- coding: utf-8 -*-
{
    'name': "cheques",

    'summary': """
        Administracion de cheques""",

    'description': """
        Lógica de negocio en el manejo de cheques. 
        En cheques propios y de terceros.
        Cheques propios.
           * Tipos de cheques (cheque común, diferidos, Cheque Cancelatorio).
           Cheque de pago común.
                
                Contenido preimpreso:
                    * Nombre del cheque en el texto.
                    * Un nro de órden incluido en el cuerpo.
                    * El nombre del banco. (En el contacto)
                    * Domicilio de pago.  (En el contacto)
                    * El nro de cuenta corriente. (En el contacto)
                    * El domiciolio que el titular tiene registrado en el Banco.
                    * El nro de cuil o cuit del titular de la cuenta.
                
                Contenido llenado en el momento de emisión.
                    * La indicación del lugar y de la fecha de creación
                    * La orden de pagar una suma determinada de dinero en número.
                    * La orden de pagar una suma determindad de dinero en letras.
                    * La firma del librador.
    Análisis Técnicos.
        A partir del recibo de pago de clientes se generará un nuevo registro en el modelo diario que contiene
        una linea más que será cheque de tercero. Este registro lo agrego con el archivo metodopago.xml
        
        Cuando se elige un cheque de tercero. Automaticamente se abre un notebook. Con los registros de movi-
        mientos de cheques. Y se carga un nuevo cheque. El total de la linea se sumará en el total del recibos.
        
        
        El modelo movimientos de cheques contendrá todos los datos relacionados a los cheques.
            Campos a generar.
                Name_del_campo          tipo        req     ro      relación.       obs    
                 Nro_orden              entero       x
                 Banco                  many2one     x              move.bank
                 Domicilio_pago         char                         
                 Domicilio_titular      char                        
                 Contacto               many2one     x              res.partner.
                 Tipo                   selección    x                              Cheque común ; Cheque diferido
                 fecha de emisión       date         x  
                 fecha de pago          date         x                              apidepens (si es comun hasta 30 días desde la emisión)
                 estado                                                             (en mano, endosado, rechazados, cobrados)
                 monto en numeros       float        x
                 monto en letras        texto        x                              apidepens (texto generado)
                 origen                 selección    x                              propio ; de tercero                 
        Debemos generar el formulario tree de cheques.
        
    """,

    'author': "Guvens",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/metododepago.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
