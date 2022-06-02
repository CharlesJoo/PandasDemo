CREATE TABLE `collection`.`data_t` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '逻辑主键',
  `year` VARCHAR(45) NULL COMMENT '年份',
  `imp_exp_flag` VARCHAR(45) NULL COMMENT '进出口标识',
  `trade_type_code` VARCHAR(45) NULL COMMENT '贸易方式代码',
  `trade_type_name` VARCHAR(45) NULL COMMENT '贸易方式名称',
  `prosumer_country_code` VARCHAR(45) NULL COMMENT '产消国代码',
  `prosumer_country_name` VARCHAR(45) NULL COMMENT '产消国名称',
  `product_code` VARCHAR(45) NULL COMMENT '商品代码',
  `product_name` VARCHAR(45) NULL COMMENT '商品名称',
  `biz_unit_code` VARCHAR(45) NULL COMMENT '经营单位代码',
  `biz_unit_name` VARCHAR(45) NULL COMMENT '经营单位名称',
  `amount` DECIMAL NULL COMMENT '金额',
  PRIMARY KEY (`id`)) ENGINE = INNODB AUTO_INCREMENT=1;
