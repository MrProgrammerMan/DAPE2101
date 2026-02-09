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
            name = "Obligatory assigment 1 - DATA2410";
            src = ./04-excercises/oblig1;
            buildInputs = [
              tex
              self'.packages.task1cplot
            ];
            phases = [ "buildPhase" "installPhase"];
            buildPhase = ''
              cp -r $src/* . #This is hella dumb, but include doesn't work otherwise
              chmod +600 ./tasks/task1
              cp ${self'.packages.task1cplot}/c.pgf ./tasks/task1
              latexmk -pdf -interaction=nonstopmode main.tex
            '';
            installPhase = ''
              mkdir -p $out
              cp main.pdf $out/
            '';
          };

          task1cplot = pkgs.stdenv.mkDerivation {
            pname = "task1cplot";
            version = "1.0";

            src = ./04-excercises/oblig1/tasks/task1;

            nativeBuildInputs = [
              pkgs.python314
              pkgs.python314Packages.matplotlib
              pkgs.python314Packages.numpy
              tex
            ];

            phases = [ "buildPhase" "installPhase" ];

            buildPhase = ''
              export MPLCONFIGDIR=$PWD/.matplotlib
              mkdir -p $MPLCONFIGDIR
              cp -r $src/* .
              python c.py
            '';

            installPhase = ''
              mkdir -p $out
              cp c.pgf $out/
            '';
          };
      };
      devShells.default = pkgs.mkShell {
        packages = with pkgs; [
          python314
          python314Packages.matplotlib
          python314Packages.numpy
        ];
      };
    };
  };
}