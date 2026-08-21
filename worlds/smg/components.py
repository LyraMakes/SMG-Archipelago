from worlds.LauncherComponents import Component, Type, components, launch

def run_client(*args: str) -> None:
    from .client.launch import launch_smg_client

    launch(launch_smg_client, name="Super Mario Galaxy Client", args=args)

components.append(
    Component(
        "Super Mario Galaxy Client",
        func=run_client,
        game_name="Super Mario Galaxy",
        component_type=Type.CLIENT,
        supports_uri=True
    )
)
