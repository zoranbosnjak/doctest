{ pkgs }:

let
  deps = with pkgs; [
    python3
  ];
  pythonDeps = with pkgs.python3Packages; [
    sphinxcontrib-applehelp
    sphinxcontrib-devhelp
    sphinxcontrib-qthelp
    sphinxcontrib-serializinghtml
    sphinxcontrib-htmlhelp
    sphinxcontrib-jsmath
    setuptools
    flit
    pygments
    Babel
    alabaster
    imagesize
    packaging
    jinja2
    snowballstemmer
    docutils
    requests
  ];

in pkgs.python3Packages.buildPythonPackage rec {
  pname = "sphinx";
  format = "pyproject";
  version = "7.0.0";
  src = pkgs.python3Packages.fetchPypi {
    pname = "Sphinx";
    inherit version;
    sha256 = "283c44aa28922bb4223777b44ac0d59af50a279ac7690dfe945bb2b9575dc41b";
  };
  propagatedBuildInputs = deps ++ pythonDeps;
  doCheck = false;
}

