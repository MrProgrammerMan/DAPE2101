{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
  };
  outputs = inputs @ { flake-parts, ... }: flake-parts.lib.mkFlake { inherit inputs; } {
    systems = [ "x86_64-linux" ];
    perSystem = { config, pkgs, self', ... }: {
      packages = 
        let 
          tex = (pkgs.texlive.withPackages (ps: with ps;[ 
            latexmk
            scheme-medium
            ps.import
            type1cm
            pgfplots
          ]));
        in {
          oblig1 = pkgs.stdenv.mkDerivation {
            name = "Obligatory assigment 1 - DAPE2101";
            src = ./04-excercises/oblig1;
            nativeBuildInputs = [
              tex
              pkgs.python314
              pkgs.python314Packages.matplotlib
              pkgs.python314Packages.numpy
            ];
            phases = [ "buildPhase" "installPhase"];
            buildPhase = ''
              export MPLCONFIGDIR=$PWD/.matplotlib
              mkdir -p $MPLCONFIGDIR
              cp -r $src/* . #This is hella dumb, but include doesn't work otherwise
              chmod -R +600 tasks
              find tasks -name '*.py' -execdir python {} \;
              latexmk -pdf -interaction=nonstopmode main.tex
            '';
            installPhase = ''
              mkdir -p $out
              cp main.pdf $out/
            '';
          };
      };
    };
  };
}
