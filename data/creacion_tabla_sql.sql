-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema supermercados
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema supermercados
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `supermercados` DEFAULT CHARACTER SET utf8mb3 ;
USE `supermercados` ;

-- -----------------------------------------------------
-- Table `supermercados`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `supermercados`.`productos` (
  `idproductos` INT NOT NULL,
  `nombre_producto` MEDIUMTEXT NOT NULL,
  `categoria` VARCHAR(45) NULL DEFAULT NULL,
  `subcategoria` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idproductos`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `supermercados`.`supermercado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `supermercados`.`supermercado` (
  `idsupermercado` INT NOT NULL,
  `nombre_supermercado` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idsupermercado`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `supermercados`.`precios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `supermercados`.`precios` (
  `idprecio` INT NOT NULL,
  `precio_unidad` DECIMAL(10,5) NULL DEFAULT NULL,
  `precio_referencia` DECIMAL(10,5) NULL DEFAULT NULL,
  `referencia` VARCHAR(45) NULL DEFAULT NULL,
  `productos_idproductos` INT NOT NULL,
  `supermercado_idsupermercado` INT NOT NULL,
  `fecha` DATE NOT NULL,
  PRIMARY KEY (`idprecio`),
  INDEX `fk_precios_productos_idx` (`productos_idproductos` ASC) VISIBLE,
  INDEX `fk_precios_supermercado1_idx` (`supermercado_idsupermercado` ASC) VISIBLE,
  CONSTRAINT `fk_precios_productos`
    FOREIGN KEY (`productos_idproductos`)
    REFERENCES `supermercados`.`productos` (`idproductos`),
  CONSTRAINT `fk_precios_supermercado1`
    FOREIGN KEY (`supermercado_idsupermercado`)
    REFERENCES `supermercados`.`supermercado` (`idsupermercado`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
