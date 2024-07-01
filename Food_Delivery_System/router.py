class DatabaseRouter:
    def db_for_read(self, model, **hints):
        """
        Read operations go to the 'default' database.
        """
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Write operations go to the 'write' database.
        """
        return 'write'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both objects are in the 'default' database.
        """
        db_list = ('default', 'write')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_syncdb(self, db, model):
        """
        Allow syncdb for the 'default' and 'write' databases.
        """
        return db in ('default', 'write')
