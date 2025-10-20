# To learn more about how to use Nix to configure your environment
# see: https://firebase.google.com/docs/studio/customize-workspace
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-25.05"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.python313
    pkgs.gnumake
  ];

  # Sets environment variables in the workspace
  env = {};
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      "ms-python.python"
      "ms-python.debugpy"
    ];

    # Enable previews
    previews = {
      enable = false;
      previews = {
      };
    };

    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
        create-venv = ''
          curl -LsSf https://astral.sh/uv/install.sh | sh
          source $HOME/.local/bin/env
        '';
      };
      # Runs when the workspace is (re)started
      onStart = {
        install-dependencies = ''
          uv sync --all-groups
          uv lock --upgrade
        '';
      };
    };
  };
}
