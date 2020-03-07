with import <nixpkgs> {};
let
  venv_dir_name = ".venv";
  pyPackages = ps: with ps; [
    pip
    setuptools
    virtualenv
  ];
  myPython = python36Full.withPackages pyPackages;
in
  pkgs.mkShell {
    buildInputs = [
      docker
      docker-compose
      git
      bashInteractive
      myPython
      postgresql
    ];
    shellHook = ''
      export SOURCE_DATE_EPOCH="$(date +%s)"

      # https://github.com/NixOS/nixpkgs/issues/66366
      export PYTHONEXECUTABLE=${venv_dir_name}/bin/python
      export PYTHONPATH=${python}/lib/python3.6/site-packages

      echo "using python: ${myPython.name}";

      echo "Ensuring python virtualenv is present.."
      if [ -d "${venv_dir_name}" ]; then
        echo "Virtualenv has been already created!"

        echo "Activating virtualenv.."
        source ${venv_dir_name}/bin/activate

        echo "Updating pip requirements."
        ${venv_dir_name}/bin/pip install -U -r timeseries_service/requirements.txt
        ${venv_dir_name}/bin/pip install -U -r stats_service/requirements.txt

        echo "Installing pip dev requirements."
        ${venv_dir_name}/bin/pip install -U -r timeseries_service/requirements-dev.txt
        ${venv_dir_name}/bin/pip install -U -r stats_service/requirements-dev.txt

        echo "Installing pip acceptance tests requirements."
        ${venv_dir_name}/bin/pip install -U -r atests/requirements.txt
        return
      fi

      echo "Creating python virtualenv.."
      virtualenv ${venv_dir_name}

      echo "Installing pip requirements."
      ${venv_dir_name}/bin/pip install -r timeseries_service/requirements.txt
      ${venv_dir_name}/bin/pip install -r stats_service/requirements.txt

      echo "Installing pip dev requirements."
      ${venv_dir_name}/bin/pip install -r timeseries_service/requirements-dev.txt
      ${venv_dir_name}/bin/pip install -r stats_service/requirements-dev.txt

      echo "Installing pip acceptance tests requirements."
      ${venv_dir_name}/bin/pip install -r atests/requirements.txt

      echo "Activating virtualenv.."
      source ${venv_dir_name}/bin/activate

      echo "Done";
    '';
}