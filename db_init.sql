CREATE TABLE `blog`.`entries` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `title` tinytext NOT NULL COMMENT '博客标题',
  `content` text NOT NULL COMMENT '博客内容',
  `posted_on` datetime(0) NOT NULL COMMENT '博客发布时间',
  PRIMARY KEY (`id`)
);