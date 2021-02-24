-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema enade
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema enade
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `enade` DEFAULT CHARACTER SET utf8 ;
USE `enade` ;

-- -----------------------------------------------------
-- Table `enade`.`Famila_participante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enade`.`Famila_participante` (
  `Escolaridade_pai` VARCHAR(100) NULL,
  `Escolaridade_mae` VARCHAR(100) NULL,
  `Com_quem_participante_mora` VARCHAR(100) NULL,
  `Quantidade_moradores_participante` VARCHAR(100) NULL,
  `Familia_cursou_superior` VARCHAR(3) NULL,
  `Renda_familia` VARCHAR(100) NULL,
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enade`.`Situação_participante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enade`.`Situação_participante` (
  `Situação_financeira` VARCHAR(100) NULL,
  `Situação_trabalho` VARCHAR(100) NULL,
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enade`.`Curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enade`.`Curso` (
  `Ingressou_cota` VARCHAR(100) NULL,
  `Motivo_ter_entrado_curso` VARCHAR(100) NULL,
  `Razão_instituição` VARCHAR(100) NULL,
  `Incetivou_graduação` VARCHAR(100) NULL,
  `Grupo_dificuldade` VARCHAR(100) NULL,
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enade`.`Escola_participante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enade`.`Escola_participante` (
  `Tipo_ensino_medio` VARCHAR(100) NULL,
  `Modalidade_ensino_medio` VARCHAR(100) NULL,
  `Regiao_concluiu_ensino_medio` VARCHAR(100) NULL,
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enade`.`Bolsa_participante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enade`.`Bolsa_participante` (
  `Bolsa_de_estudo` VARCHAR(100) NULL,
  `Bolsa_permanência` VARCHAR(100) NULL,
  `Bolsa_acadêmica` VARCHAR(100) NULL,
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enade`.`Preparação_participante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enade`.`Preparação_participante` (
  `Atividade_exterior` VARCHAR(100) NULL,
  `Livro_lido_ano` VARCHAR(100) NULL,
  `Horas_por_semana_estudou` VARCHAR(100) NULL,
  `Estudou_idioma_estrangeiro` VARCHAR(100) NULL,
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `enade`.`Participante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `enade`.`Participante` (
  `idade` INT NULL,
  `Sexo` VARCHAR(20) NULL,
  `Nota_geral` DOUBLE NULL,
  `Estado_civil` VARCHAR(100) NULL,
  `Raça` VARCHAR(100) NULL,
  `Nacionalidade` VARCHAR(100) NULL,
  `Id_participante` INT NOT NULL,
  `Famila_participante_id` INT UNSIGNED NOT NULL,
  `Situação_participante_id` INT UNSIGNED NOT NULL,
  `Curso_id` INT UNSIGNED NOT NULL,
  `Escola_participante_id` INT UNSIGNED NOT NULL,
  `Bolsa_participante_id` INT UNSIGNED NOT NULL,
  `Preparação_participante_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Id_participante`),
  UNIQUE INDEX `Id_participante_UNIQUE` (`Id_participante` ASC) VISIBLE,
  INDEX `fk_Participante_Famila_participante_idx` (`Famila_participante_id` ASC) VISIBLE,
  INDEX `fk_Participante_Situação_participante1_idx` (`Situação_participante_id` ASC) VISIBLE,
  INDEX `fk_Participante_Curso1_idx` (`Curso_id` ASC) VISIBLE,
  INDEX `fk_Participante_Escola_participante1_idx` (`Escola_participante_id` ASC) VISIBLE,
  INDEX `fk_Participante_Bolsa_participante1_idx` (`Bolsa_participante_id` ASC) VISIBLE,
  INDEX `fk_Participante_Preparação_participante1_idx` (`Preparação_participante_id` ASC) VISIBLE,
  CONSTRAINT `fk_Participante_Famila_participante`
    FOREIGN KEY (`Famila_participante_id`)
    REFERENCES `enade`.`Famila_participante` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Participante_Situação_participante1`
    FOREIGN KEY (`Situação_participante_id`)
    REFERENCES `enade`.`Situação_participante` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Participante_Curso1`
    FOREIGN KEY (`Curso_id`)
    REFERENCES `enade`.`Curso` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Participante_Escola_participante1`
    FOREIGN KEY (`Escola_participante_id`)
    REFERENCES `enade`.`Escola_participante` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Participante_Bolsa_participante1`
    FOREIGN KEY (`Bolsa_participante_id`)
    REFERENCES `enade`.`Bolsa_participante` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Participante_Preparação_participante1`
    FOREIGN KEY (`Preparação_participante_id`)
    REFERENCES `enade`.`Preparação_participante` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
