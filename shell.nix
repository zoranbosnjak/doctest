{ sources ? import ./nix/sources.nix
, pkgs ? import sources.nixpkgs {}
, gitrev ? "devel"
, inShell ? null
}:

let
  tex = pkgs.texlive.combined.scheme-full;

  sphinx = pkgs.callPackage ./nix/sphinx { inherit pkgs; };

  deps = with pkgs; [
    git
    sphinx
    tex
  ];

  fontconf = pkgs.makeFontsConf { fontDirectories = [
    pkgs.dejavu_fonts
  ]; };

  envVars = ''
    export GITREV="${gitrev}"
    export LOCALE_ARCHIVE="${pkgs.glibcLocales}/lib/locale/locale-archive"
  '';

  src = builtins.filterSource
    (path: type:
      (type != "directory" || baseNameOf path != ".git")
      && (type != "symlink" || baseNameOf path != "result"))
    ./.;

  env = pkgs.stdenv.mkDerivation {
    name = "test-environment";
    buildInputs = deps;
    shellHook = envVars;
    FONTCONFIG_FILE = fontconf;
  };

in {
  output = env;
  inherit pkgs;
}

