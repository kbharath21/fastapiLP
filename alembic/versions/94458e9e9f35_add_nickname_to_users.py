from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "94458e9e9f35"
down_revision = "c47ecbf163d4"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "users",
        sa.Column("nickname", sa.String(), nullable=True),
    )


def downgrade():
    op.drop_column("users", "nickname")
