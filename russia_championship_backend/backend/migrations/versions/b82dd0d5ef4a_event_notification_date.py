"""event_notification Date

Revision ID: b82dd0d5ef4a
Revises: 
Create Date: 2024-11-23 14:34:51.776975

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b82dd0d5ef4a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('countrys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('country_name')
    )
    op.create_table('discipline',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('discipline_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('discipline_name')
    )
    op.create_table('sex',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sex', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sex')
    )
    op.create_table('type_championship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('type_name')
    )
    op.create_table('type_sport',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('type_name')
    )
    op.create_table('subjects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject_name', sa.String(), nullable=True),
    sa.Column('id_country', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_country'], ['countrys.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('subject_name')
    )
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city_name', sa.String(), nullable=True),
    sa.Column('id_subject', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_subject'], ['subjects.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('city_name')
    )
    op.create_index('city_name_index', 'city', ['city_name'], unique=False)
    op.create_table('events',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('date_start', sa.Date(), nullable=True),
    sa.Column('date_end', sa.Date(), nullable=True),
    sa.Column('photo_url', sa.String(), nullable=True),
    sa.Column('count', sa.String(), nullable=True),
    sa.Column('id_type_championship', sa.Integer(), nullable=True),
    sa.Column('id_type_sport', sa.Integer(), nullable=True),
    sa.Column('id_city', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_city'], ['city.id'], ),
    sa.ForeignKeyConstraint(['id_type_championship'], ['type_championship.id'], ),
    sa.ForeignKeyConstraint(['id_type_sport'], ['type_sport.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('type_sport_index', 'events', ['id_type_sport'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('FIO', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('single_mode_code', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('photo_url', sa.String(), nullable=True),
    sa.Column('google_access_token', sa.String(), nullable=True),
    sa.Column('yandex_access_token', sa.String(), nullable=True),
    sa.Column('telegram_id', sa.String(), nullable=True),
    sa.Column('is_coach', sa.Boolean(), nullable=False),
    sa.Column('birthday_date', sa.DateTime(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('about', sa.String(), nullable=True),
    sa.Column('id_city', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_city'], ['city.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index('email_index', 'user', ['email'], unique=False)
    op.create_table('events_discipline',
    sa.Column('event_id', sa.String(), nullable=False),
    sa.Column('discipline_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['discipline_id'], ['discipline.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('event_id', 'discipline_id')
    )
    op.create_table('events_notification',
    sa.Column('event_id', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('count_days', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('event_id', 'user_id')
    )
    op.create_table('events_sex',
    sa.Column('event_id', sa.String(), nullable=False),
    sa.Column('sex_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sex_id'], ['sex.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('event_id', 'sex_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events_sex')
    op.drop_table('events_notification')
    op.drop_table('events_discipline')
    op.drop_index('email_index', table_name='user')
    op.drop_table('user')
    op.drop_index('type_sport_index', table_name='events')
    op.drop_table('events')
    op.drop_index('city_name_index', table_name='city')
    op.drop_table('city')
    op.drop_table('subjects')
    op.drop_table('type_sport')
    op.drop_table('type_championship')
    op.drop_table('sex')
    op.drop_table('discipline')
    op.drop_table('countrys')
    # ### end Alembic commands ###
