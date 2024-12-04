import s_taper as s_t
from s_taper.consts import *

base = {
    "user_id": INT + KEY

}

users = s_t.Taper("users", "data.db").create_table(base)